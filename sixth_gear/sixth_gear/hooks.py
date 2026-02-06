app_name = "sixth_gear"
app_title = "Sixth Gear"
app_publisher = "Jules"
app_description = "Sixth Gear: A hybrid LifeOS and Second Brain Frappe App"
app_email = "jules@example.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sixth_gear/css/sixth_gear.css"
app_include_js = "/assets/sixth_gear/js/focus_mode.js"

# include js, css files in header of web template
# web_include_css = "/assets/sixth_gear/css/sixth_gear.css"
# web_include_js = "/assets/sixth_gear/js/sixth_gear.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# "Guest": "blog",
# "System Manager": "/app/home-base"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "sixth_gear.install.before_install"
# after_install = "sixth_gear.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "sixth_gear.uninstall.before_uninstall"
# after_uninstall = "sixth_gear.uninstall.after_uninstall"

# Integration Setup
# ------------------

# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "sixth_gear.utils.before_app_install"
# after_app_install = "sixth_gear.utils.after_app_install"

# Integration Cleanup
# -------------------

# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "sixth_gear.utils.before_app_uninstall"
# after_app_uninstall = "sixth_gear.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sixth_gear.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
	"daily": [
		"sixth_gear.sixth_gear.scheduled_tasks.generate_recurring_tasks",
		"sixth_gear.integrations.fetch_readwise"
	],
}

# Testing
# -------

# before_tests = "sixth_gear.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sixth_gear.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "sixth_gear.task.get_dashboard_data"
# }

# git_url = "https://github.com/jules/sixth_gear"

# Security Settings (Rate Limiting)
# ---------------------------------
# Limit the number of requests per window.
# window is in seconds, limit is number of requests.

rate_limit = {"limit": 600, "window": 3600}

# CAPTCHA
# -------
# Google reCAPTCHA settings should be set in site_config.json,
# but we can ensure the hook for validation is present if needed.
# For standard Login, Frappe handles this via System Settings.

# PWA
# ---
pwa_manifest = {
	"name": "Sixth Gear",
	"short_name": "SixthGear",
	"description": "Hybrid Productivity System",
	"start_url": "/app/home-base",
	"display": "standalone",
	"background_color": "#ffffff",
	"theme_color": "#171717"
}
