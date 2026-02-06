import frappe
from frappe.model.document import Document
from frappe.utils import flt

class Goal(Document):
	def validate(self):
		self.calculate_progress()

	def calculate_progress(self):
		# 1. Child Goals
		child_goals = frappe.get_all("Goal", filters={"parent_goal": self.name}, fields=["progress"])

		# 2. Linked Projects
		linked_projects = frappe.get_all("Project", filters={"goal": self.name}, fields=["name"])

		total_items = len(child_goals) + len(linked_projects)
		if total_items == 0:
			# If no children, progress is manual or 0? Leaving as is if manual, otherwise 0.
			# For now, let's say if no children, respect manual input or default to 0.
			# But field is read_only. So it stays 0 unless we have logic.
			# Let's assume if leaf node, progress is 0 unless manually updated (but field is read only).
			# Update: If it's a leaf goal, maybe we should allow manual entry?
			# The schema says 'read_only': 1. So it MUST be calculated.
			self.progress = 0
			return

		sum_progress = 0

		for g in child_goals:
			sum_progress += flt(g.progress)

		for p_ref in linked_projects:
			p = frappe.get_doc("Project", p_ref.name)
			sum_progress += flt(p.progress) # p.progress is a property in Project doc

		self.progress = sum_progress / total_items

		# Update status based on progress? Optional.
		if self.progress == 100:
			self.status = "Completed"

	def on_update(self):
		# Roll up to parent
		if self.parent_goal:
			parent = frappe.get_doc("Goal", self.parent_goal)
			parent.calculate_progress()
			parent.save()
