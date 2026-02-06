import frappe
from frappe.utils import add_days, add_months, getdate, today

def generate_recurring_tasks():
    # Find tasks that are recurring, active, and due for generation
    tasks = frappe.get_all("Task", filters={
        "is_recurring": 1,
        "status": ["in", ["Open", "Working"]], # Only active templates
        "next_due_date": ["<=", today()]
    })

    for t in tasks:
        original_task = frappe.get_doc("Task", t.name)

        # Create the new instance
        new_task = frappe.copy_doc(original_task)
        new_task.is_recurring = 0
        new_task.due_date = original_task.next_due_date
        new_task.next_due_date = None
        new_task.status = "Open"
        new_task.insert(ignore_permissions=True)

        # Update the original task's next_due_date
        next_date = getdate(original_task.next_due_date)

        if original_task.frequency == "Daily":
            next_date = add_days(next_date, 1)
        elif original_task.frequency == "Weekly":
            next_date = add_days(next_date, 7)
        elif original_task.frequency == "Monthly":
            next_date = add_months(next_date, 1)

        original_task.next_due_date = next_date
        original_task.save(ignore_permissions=True)

        frappe.db.commit()
