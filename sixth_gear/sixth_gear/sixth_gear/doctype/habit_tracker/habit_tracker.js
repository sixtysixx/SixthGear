frappe.ui.form.on('Habit Tracker', {
	refresh: function(frm) {
		frm.trigger('render_chart');
	},

	render_chart: function(frm) {
		if (!frm.doc.logs || frm.doc.logs.length === 0) return;

		let data = [];
		let labels = [];

		// Prepare data for the last 30 days or so
		// Since we can't easily do complex date math in JS without library,
		// we will just visualize the logs we have.

		// Sort logs by date ascending
		let logs = frm.doc.logs.slice().sort((a, b) => new Date(a.date) - new Date(b.date));

		// Take last 30 entries
		logs = logs.slice(-30);

		logs.forEach(log => {
			labels.push(log.date);
			data.push(log.status === 'Completed' ? 1 : 0);
		});

		frm.dashboard.add_widget({
			type: 'bar',
			data: {
				labels: labels,
				datasets: [
					{
						name: "Completion",
						values: data
					}
				]
			},
			title: 'Recent Activity',
			colors: ['#31d06e']
		});
	}
});
