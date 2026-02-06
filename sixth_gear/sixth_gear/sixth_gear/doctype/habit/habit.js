// Copyright (c) 2024, Sixth Gear and contributors
// For license information, please see license.txt

frappe.ui.form.on('Habit', {
	refresh: function(frm) {
		if (!frm.is_new() && frm.doc.status !== 'Archived') {
			frm.add_custom_button(__('Check In'), function() {
				frm.call({
					method: 'check_in',
					freeze: true,
					callback: function(r) {
						if (!r.exc) {
							frm.reload_doc();
						}
					}
				});
			}).addClass('btn-primary');
		}

		if (!frm.is_new()) {
			frm.call('get_history').then(r => {
				if (r.message) {
					let wrapper = $(frm.dashboard.wrapper).find('.habit-heatmap');
					if (wrapper.length === 0) {
						$('<div class="habit-heatmap" style="margin-top: 20px; border: 1px solid #d1d8dd; border-radius: 4px; padding: 15px;"></div>').appendTo(frm.dashboard.wrapper);
						wrapper = $(frm.dashboard.wrapper).find('.habit-heatmap');
					} else {
						wrapper.empty();
					}

					new frappe.Chart(wrapper[0], {
						type: 'heatmap',
						title: 'Completion History',
						data: {
							dataPoints: r.message
						},
						countLabel: 'Completions',
						discreteDomains: 1,
						colors: ['#ebedf0', '#9be9a8', '#40c463', '#30a14e', '#216e39']
					});
				}
			});
		}
	}
});
