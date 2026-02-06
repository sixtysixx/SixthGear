import frappe
from frappe.model.document import Document
from frappe.utils import add_days, add_months, today, getdate

class Task(Document):
    def validate(self):
        if self.priority == "High":
            self.color = "#ff4d4d"  # Red
        elif self.priority == "Medium":
            self.color = "#ffbf00"  # Orange
        elif self.priority == "Low":
            self.color = "#4d94ff"  # Blue

        if self.is_recurring and not self.next_due_date:
            # Set initial next_due_date if not set
            if self.due_date:
                 self.next_due_date = self.due_date
            else:
                 self.next_due_date = today()

    def on_update(self):
        if self.reference_doctype == "Project" and self.reference_name:
            # We need to find the Project and trigger its Goal update
            # We can't just call project.save() as it might be recursive or heavy
            # Instead we load project to check if it has a goal
            try:
                project = frappe.get_doc("Project", self.reference_name)
                if project.goal:
                    goal = frappe.get_doc("Goal", project.goal)
                    goal.calculate_progress()
                    goal.save()
            except frappe.DoesNotExistError:
                pass
