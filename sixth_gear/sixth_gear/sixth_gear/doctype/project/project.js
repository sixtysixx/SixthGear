frappe.ui.form.on('Project', {
	refresh: function(frm) {
		if (!frm.is_new()) {
			// Render Dashboard
			frm.call({
				method: 'get_dashboard_data',
				doc: frm.doc,
				callback: function(r) {
					if (r.message) {
						render_dashboard(frm, r.message);
					}
				}
			});

			// Render Progress Bar (Simulated calculation from client side for immediate feedback,
			// though the backend property exists for reliable data)
			frappe.db.count('Task', {
				reference_doctype: 'Project',
				reference_name: frm.doc.name
			}).then(total => {
				if (total > 0) {
					frappe.db.count('Task', {
						reference_doctype: 'Project',
						reference_name: frm.doc.name,
						status: 'Completed'
					}).then(completed => {
						let percent = Math.round((completed / total) * 100);
						let html = `
							<div class="progress" style="height: 20px;">
								<div class="progress-bar bg-success" role="progressbar" style="width: ${percent}%;" aria-valuenow="${percent}" aria-valuemin="0" aria-valuemax="100">${percent}%</div>
							</div>
						`;
						frm.set_df_property('progress_html', 'options', html);
					});
				} else {
					frm.set_df_property('progress_html', 'options', '<p class="text-muted">No tasks linked.</p>');
				}
			});
		}
	}
});

function render_dashboard(frm, data) {
	let tasks_html = data.tasks.length ?
		`<table class="table table-bordered">
			<thead><tr><th>Task</th><th>Due</th><th>Priority</th></tr></thead>
			<tbody>
				${data.tasks.map(t => `
					<tr>
						<td><a href="/app/task/${t.name}">${t.subject}</a></td>
						<td>${frappe.datetime.str_to_user(t.due_date)}</td>
						<td>${t.priority}</td>
					</tr>
				`).join('')}
			</tbody>
		</table>` : '<p>No active tasks.</p>';

	let knowledge_html = `
		<h5>Notes</h5>
		<ul>
			${data.notes.length ? data.notes.map(n => `<li><a href="/app/note/${n.name}">${n.title}</a> (${n.workflow_state})</li>`).join('') : '<li>No notes found.</li>'}
		</ul>
		<h5>Resources</h5>
		<ul>
			${data.resources.length ? data.resources.map(r => `<li><a href="/app/resource/${r.name}">${r.resource_name}</a></li>`).join('') : '<li>No resources found.</li>'}
		</ul>
	`;

	let html = `
		<div class="row">
			<div class="col-md-6">
				<h4>Action List</h4>
				${tasks_html}
			</div>
			<div class="col-md-6">
				<h4>Knowledge Context</h4>
				${knowledge_html}
			</div>
		</div>
	`;

	frm.set_df_property('project_hub', 'options', html);
}
