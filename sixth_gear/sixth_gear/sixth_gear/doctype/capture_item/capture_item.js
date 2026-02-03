frappe.ui.form.on('Capture Item', {
    refresh: function(frm) {
        if (frm.doc.status === "Open" && !frm.is_new()) {
            frm.add_custom_button(__('Convert to Task'), function() {
                frappe.call({
                    doc: frm.doc,
                    method: 'convert_to_task',
                    callback: function(r) {
                        if (r.message) {
                            frappe.set_route('Form', 'Task', r.message);
                        }
                    }
                });
            }, __('Actions'));

            frm.add_custom_button(__('Convert to Note'), function() {
                frappe.call({
                    doc: frm.doc,
                    method: 'convert_to_note',
                    callback: function(r) {
                        if (r.message) {
                            frappe.set_route('Form', 'Note', r.message);
                        }
                    }
                });
            }, __('Actions'));
        }
    }
});
