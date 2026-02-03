import frappe
from frappe.model.document import Document

class CaptureItem(Document):
    @frappe.whitelist()
    def convert_to_task(self):
        task = frappe.new_doc("Task")
        task.subject = self.content
        task.description = self.content
        task.insert()

        self.status = "Converted"
        self.save()
        return task.name

    @frappe.whitelist()
    def convert_to_note(self):
        note = frappe.new_doc("Note")
        note.title = self.content[:50] # First 50 chars as title
        note.capture = self.content
        note.insert()

        self.status = "Converted"
        self.save()
        return note.name
