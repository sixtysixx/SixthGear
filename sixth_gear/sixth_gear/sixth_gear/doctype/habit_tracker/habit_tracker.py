import frappe
from frappe.model.document import Document
from frappe.utils import getdate, add_days, get_first_day_of_week

class HabitTracker(Document):
	def validate(self):
		self.calculate_streak()

	def calculate_streak(self):
		if not self.logs:
			self.streak = 0
			return

		# Sort logs by date descending
		sorted_logs = sorted(self.logs, key=lambda x: getdate(x.date), reverse=True)

		if not sorted_logs:
			self.streak = 0
			return

		self.last_completed = sorted_logs[0].date

		if self.frequency == "Daily":
			self.calculate_daily_streak(sorted_logs)
		elif self.frequency == "Weekly":
			self.calculate_weekly_streak(sorted_logs)

	def calculate_daily_streak(self, sorted_logs):
		streak = 0
		current_date = getdate(sorted_logs[0].date)

		# Check if the last log is today or yesterday
		today = getdate()
		diff = (today - current_date).days

		if diff > 1:
			self.streak = 0
			return

		# Count consecutive days
		expected_date = current_date
		for log in sorted_logs:
			if log.status == "Completed":
				log_date = getdate(log.date)
				if log_date == expected_date:
					streak += 1
					expected_date = add_days(expected_date, -1)
				elif log_date > expected_date:
					continue
				else:
					break
			else:
				# If skipped/missed, break streak (simplified logic)
				break

		self.streak = streak

	def calculate_weekly_streak(self, sorted_logs):
		streak = 0
		last_log_date = getdate(sorted_logs[0].date)

		# Check if last completion was this week or last week
		today = getdate()
		current_week_start = get_first_day_of_week(today)
		last_log_week_start = get_first_day_of_week(last_log_date)

		weeks_diff = (current_week_start - last_log_week_start).days / 7

		if weeks_diff > 1:
			self.streak = 0
			return

		# Iterate backwards by week
		# We need to group logs by week
		completed_weeks = set()
		for log in sorted_logs:
			if log.status == "Completed":
				log_week_start = get_first_day_of_week(getdate(log.date))
				completed_weeks.add(log_week_start)

		# Calculate consecutive weeks
		expected_week = last_log_week_start
		streak = 0

		# We rely on the set logic.
		# If we have 5 completed weeks, check if they are consecutive.
		# But since we iterate backwards from 'last_log_week_start', we just check existence.

		while expected_week in completed_weeks:
			streak += 1
			expected_week = add_days(expected_week, -7)

		self.streak = streak
