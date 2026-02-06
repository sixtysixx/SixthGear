import frappe
import requests
from frappe.utils import now_datetime

def fetch_readwise():
    settings = frappe.get_single("Readwise Settings")
    if not settings.is_enabled or not settings.api_key:
        return

    # Check for last sync date
    last_sync = settings.last_sync or "2000-01-01T00:00:00Z"

    headers = {"Authorization": f"Token {settings.api_key}"}

    # Get highlights
    # This is a simplified implementation. Real Readwise API has pagination.
    # Endpoint: https://readwise.io/api/v2/highlights/
    try:
        response = requests.get(
            "https://readwise.io/api/v2/highlights/",
            headers=headers,
            params={"updated_after": last_sync},
            timeout=10
        )

        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])

            # Group by book_id? The results have book_id.
            # We need to fetch books too to get titles.
            # For this MVP, let's assume we just capture them as generic notes or fetch book details if needed.
            # To save API calls, maybe we just dump them into an Inbox Note per sync?
            # Or better: "Readwise Import {Date}"

            if results:
                note_content = ""
                for h in results:
                    text = h.get("text", "")
                    title = h.get("title", "Unknown Source") # Highlights usually don't have title in the list, need expansion.
                    # Actually, results list usually just has text, note, book_id.
                    # We would need to fetch book metadata.
                    # For MVP, let's just log the text.
                    note_content += f"<blockquote>{text}</blockquote><br><br>"

                # Create a Note
                note = frappe.new_doc("Note")
                note.title = f"Readwise Import {now_datetime().strftime('%Y-%m-%d %H:%M')}"
                note.capture = note_content
                note.workflow_state = "Inbox"
                note.insert(ignore_permissions=True)

                # Update last sync
                settings.last_sync = now_datetime()
                settings.save()

    except Exception as e:
        frappe.log_error(f"Readwise Sync Failed: {str(e)}")
