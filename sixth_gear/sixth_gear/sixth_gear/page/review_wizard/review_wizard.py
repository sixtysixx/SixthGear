import frappe
from frappe.utils import nowdate

@frappe.whitelist()
def save_review(type, data):
	data = frappe.parse_json(data)
	content = ""
	for key, value in data.items():
		content += f"**{key.replace('_', ' ').title()}**: {value}\n\n"

	note = frappe.get_doc({
		"doctype": "Note",
		"title": f"{type} Review - {nowdate()}",
		"capture": content,
		"workflow_state": "Organized" # Directly organized
	})
	note.insert()
