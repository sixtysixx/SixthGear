app_name = "syx"
app_title = "Syx"
app_publisher = "Jules"
app_description = "Syx: A hybrid LifeOS and Second Brain Frappe App"
app_email = "jules@example.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/syx/css/syx.css"
app_include_js = "/assets/syx/js/focus_mode.js"

# include js, css files in header of web template
# web_include_css = "/assets/syx/css/syx.css"
# web_include_js = "/assets/syx/js/syx.js"

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

# before_install = "syx.install.before_install"
# after_install = "syx.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "syx.uninstall.before_uninstall"
# after_uninstall = "syx.uninstall.after_uninstall"

# Integration Setup
# ------------------

# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "syx.utils.before_app_install"
# after_app_install = "syx.utils.after_app_install"

# Integration Cleanup
# -------------------

# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "syx.utils.before_app_uninstall"
# after_app_uninstall = "syx.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "syx.notifications.get_notification_config"

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
		"syx.syx.scheduled_tasks.generate_recurring_tasks",
		"syx.integrations.fetch_readwise"
	],
}

# Testing
# -------

# before_tests = "syx.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "syx.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "syx.task.get_dashboard_data"
# }

# git_url = "https://github.com/jules/syx"

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
	"name": "Syx",
	"short_name": "Syx",
	"description": "Hybrid Productivity System",
	"start_url": "/app/home-base",
	"display": "standalone",
	"background_color": "#ffffff",
	"theme_color": "#171717"
}
