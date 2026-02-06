frappe.pages['review-wizard'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Review Wizard',
		single_column: true
	});

	page.main.html('<div class="review-wizard-container" style="padding: 20px;"></div>');
	let $container = $(page.main).find('.review-wizard-container');

	let render_home = () => {
		$container.html(`
			<div class="row">
				<div class="col-md-6">
					<div class="card" style="padding: 20px; cursor: pointer;" id="morning-review-btn">
						<h3>☀️ Morning Review</h3>
						<p>Plan your day, check your calendar, and set intentions.</p>
					</div>
				</div>
				<div class="col-md-6">
					<div class="card" style="padding: 20px; cursor: pointer;" id="evening-review-btn">
						<h3>🌙 Evening Review</h3>
						<p>Reflect on your achievements and clear your inbox.</p>
					</div>
				</div>
			</div>
		`);

		$('#morning-review-btn').click(() => start_review('Morning'));
		$('#evening-review-btn').click(() => start_review('Evening'));
	};

	let start_review = (type) => {
		let fields = [];
		if (type === 'Morning') {
			fields = [
				{'label': 'What are your 3 main tasks today?', 'fieldname': 'tasks', 'fieldtype': 'Small Text', 'reqd': 1},
				{'label': 'Any blocked tasks?', 'fieldname': 'blockers', 'fieldtype': 'Small Text'}
			];
		} else {
			fields = [
				{'label': 'What did you achieve today?', 'fieldname': 'achievements', 'fieldtype': 'Small Text', 'reqd': 1},
				{'label': 'Pending items for tomorrow', 'fieldname': 'pending', 'fieldtype': 'Small Text'}
			];
		}

		let d = new frappe.ui.Dialog({
			title: type + ' Review',
			fields: fields,
			primary_action_label: 'Complete Review',
			primary_action: function(values) {
				frappe.call({
					method: 'syx.syx.page.review_wizard.review_wizard.save_review',
					args: {
						type: type,
						data: values
					},
					callback: function(r) {
						if (!r.exc) {
							d.hide();
							frappe.msgprint('Review Saved!');
							render_home();
						}
					}
				});
			}
		});
		d.show();
	};

	render_home();
};
