import frappe
from frappe.model.document import Document
import os
import requests

class CaptureItem(Document):
    @frappe.whitelist()
    def convert_to_task(self):
        task = frappe.new_doc("Task")
        task.subject = self.title or self.content[:50]
        task.description = self.content
        task.insert()

        self.status = "Converted"
        self.save()
        return task.name

    @frappe.whitelist()
    def convert_to_note(self):
        note = frappe.new_doc("Note")
        note.title = self.title or self.content[:50]
        note.capture = self.content
        note.insert()

        self.status = "Converted"
        self.save()
        return note.name

    @frappe.whitelist()
    def transcribe_audio(self):
        if not self.audio_file:
            frappe.throw("No audio file attached")

        settings = frappe.get_single("Voice Settings")
        api_key = settings.get_password("openai_api_key")

        if not api_key:
            frappe.throw("OpenAI API Key not configured in Voice Settings")

        file_doc = frappe.get_doc("File", {"file_url": self.audio_file})
        file_path = file_doc.get_full_path()

        headers = {
            "Authorization": f"Bearer {api_key}"
        }

        try:
            # We open the file and send it
            with open(file_path, "rb") as f:
                files = {
                    "file": (file_doc.file_name, f, "application/octet-stream")
                }
                data = {
                    "model": settings.model or "whisper-1"
                }

                response = requests.post(
                    "https://api.openai.com/v1/audio/transcriptions",
                    headers=headers,
                    files=files,
                    data=data,
                    timeout=60
                )

            if response.status_code == 200:
                result = response.json()
                self.transcription = result.get("text", "")
                self.content = (self.content or "") + "\n\nTranscription:\n" + self.transcription
                self.save()
                frappe.msgprint("Transcription Complete")
            else:
                frappe.throw(f"OpenAI Error: {response.text}")

        except Exception as e:
             frappe.log_error(f"Whisper Error: {str(e)}")
             frappe.throw(f"Transcription failed: {str(e)}")

    @staticmethod
    def make_from_email(email):
        """
        Called by Email Account when an email is received for this DocType.
        email: frappe.email.receive.Email object
        """
        doc = frappe.new_doc("Capture Item")
        doc.title = email.subject
        doc.content = email.content
        doc.source = "Email"
        doc.insert(ignore_permissions=True)
        return doc
