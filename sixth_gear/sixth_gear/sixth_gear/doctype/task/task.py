import frappe
from frappe.model.document import Document


class Task(Document):
    def validate(self):
        if self.priority == "High":
            self.color = "#ff4d4d"  # Red
        elif self.priority == "Medium":
            self.color = "#ffbf00"  # Orange
        elif self.priority == "Low":
            self.color = "#4d94ff"  # Blue
