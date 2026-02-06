import frappe
from frappe.model.document import Document


class Project(Document):
    @frappe.whitelist()
    def get_dashboard_data(self):
        # Action List: Incomplete Tasks
        tasks = frappe.get_all(
            "Task",
            filters={
                "reference_doctype": "Project",
                "reference_name": self.name,
                "status": ["!=", "Completed"],
            },
            fields=["name", "subject", "due_date", "priority", "status"],
        )

        # Knowledge Context: Notes and Resources
        notes = frappe.get_all(
            "Note",
            filters={"project": self.name},
            fields=["name", "title", "workflow_state"],
        )

        resources = frappe.get_all(
            "Resource", filters={"project": self.name}, fields=["name", "resource_name"]
        )

        return {"tasks": tasks, "notes": notes, "resources": resources}

    @property
    def progress(self):
        total_tasks = frappe.db.count(
            "Task", {"reference_doctype": "Project", "reference_name": self.name}
        )

        if total_tasks == 0:
            return 0

        completed_tasks = frappe.db.count(
            "Task",
            {
                "reference_doctype": "Project",
                "reference_name": self.name,
                "status": "Completed",
            },
        )

        return (completed_tasks / total_tasks) * 100

    def on_update(self):
        if self.goal:
            g = frappe.get_doc("Goal", self.goal)
            g.calculate_progress()
            g.save()
