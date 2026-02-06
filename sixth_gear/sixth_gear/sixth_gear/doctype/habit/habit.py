import frappe
from frappe.model.document import Document
from frappe.utils import getdate, today, add_days

class Habit(Document):
	@frappe.whitelist()
	def check_in(self):
		# Check if already checked in today
		existing = frappe.db.exists("Habit Log", {
			"habit": self.name,
			"date": today()
		})

		if existing:
			frappe.msgprint("Already checked in today!")
			return

		doc = frappe.get_doc({
			"doctype": "Habit Log",
			"habit": self.name,
			"date": today()
		})
		doc.insert()
		frappe.msgprint(f"Checked in for {self.title}!")
		# streak update handled by Habit Log after_insert

	def update_streak(self):
		logs = frappe.get_all("Habit Log", filters={"habit": self.name}, fields=["date"], order_by="date desc")

		if not logs:
			self.current_streak = 0
			self.longest_streak = 0
			self.total_completions = 0
			self.last_checkin = None
			return

		# Unique dates
		dates = sorted(list(set([getdate(l.date) for l in logs])), reverse=True)

		self.last_checkin = dates[0]
		self.total_completions = len(dates)

		# Current Streak
		current_streak = 0
		today_date = getdate(today())

		# If the last checkin was today or yesterday, the streak is alive
		if dates[0] == today_date or dates[0] == add_days(today_date, -1):
			current_streak = 1
			previous_date = dates[0]

			for i in range(1, len(dates)):
				if dates[i] == add_days(previous_date, -1):
					current_streak += 1
					previous_date = dates[i]
				else:
					break
		else:
			current_streak = 0

		self.current_streak = current_streak

		# Longest Streak calculation
		longest_streak = 1 if dates else 0
		temp_streak = 1
		for i in range(len(dates) - 1):
			if dates[i+1] == add_days(dates[i], -1):
				temp_streak += 1
			else:
				if temp_streak > longest_streak:
					longest_streak = temp_streak
				temp_streak = 1

		if temp_streak > longest_streak:
			longest_streak = temp_streak

		self.longest_streak = longest_streak

	@frappe.whitelist()
	def get_history(self):
		logs = frappe.get_all("Habit Log", filters={"habit": self.name}, fields=["date", "timestamp"])
		# Format for Heatmap: timestamp (seconds), count
		data = {}
		for l in logs:
			# Use the timestamp field for precise time, or just date
			# Frappe Charts Heatmap expects unix timestamp
			ts = int(l.timestamp.timestamp())
			data[ts] = 1
		return data
