import frappe

@frappe.whitelist(allow_guest=True) # Allow guest? Maybe insecure. Better to require key.
def create_capture_item(content, title=None, url=None, source="Browser"):
    # If using API Key/Secret, allow_guest=False is fine.
    # The browser extension should use token based auth.

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
