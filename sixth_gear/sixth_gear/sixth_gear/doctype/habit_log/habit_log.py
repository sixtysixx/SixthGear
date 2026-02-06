import frappe
from frappe.model.document import Document

class HabitLog(Document):
	def after_insert(self):
		if frappe.get_meta("Habit").has_field("current_streak"): # Basic check to ensure Habit doctype exists and is updated
			habit = frappe.get_doc("Habit", self.habit)
			habit.update_streak()
			habit.save()
