import frappe

@frappe.whitelist(allow_guest=False)
def create_capture_item(content, title=None, url=None, source="Browser"):
    # Requires Authorization: token <api_key>:<api_secret>

    if not content:
        frappe.throw("Content is required")

    full_content = content
    if url:
        full_content += f"\n\nSource: {url}"

    doc = frappe.get_doc({
        "doctype": "Capture Item",
        "title": title or content[:50],
        "content": full_content,
        "source": source
    })
    doc.insert(ignore_permissions=True)
    return {"name": doc.name}
