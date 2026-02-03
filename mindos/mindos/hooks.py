app_name = "mindos"
app_title = "MindOS"
app_publisher = "Jules"
app_description = "MindOS: A hybrid LifeOS and Second Brain Frappe App"
app_email = "jules@example.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mindos/css/mindos.css"
# app_include_js = "/assets/mindos/js/mindos.js"

# include js, css files in header of web template
# web_include_css = "/assets/mindos/css/mindos.css"
# web_include_js = "/assets/mindos/js/mindos.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Guest": "blog",
#	"System Manager": "/app/home-base"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "mindos.install.before_install"
# after_install = "mindos.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "mindos.uninstall.before_uninstall"
# after_uninstall = "mindos.uninstall.after_uninstall"

# Integration Setup
# ------------------

# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "mindos.utils.before_app_install"
# after_app_install = "mindos.utils.after_app_install"

# Integration Cleanup
# -------------------

# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "mindos.utils.before_app_uninstall"
# after_app_uninstall = "mindos.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mindos.notifications.get_notification_config"

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

# scheduler_events = {
# 	"all": [
# 		"mindos.tasks.all"
# 	],
# 	"daily": [
# 		"mindos.tasks.daily"
# 	],
# 	"hourly": [
# 		"mindos.tasks.hourly"
# 	],
# 	"weekly": [
# 		"mindos.tasks.weekly"
# 	],
# 	"monthly": [
# 		"mindos.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "mindos.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "mindos.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "mindos.task.get_dashboard_data"
# }

# git_url = "https://github.com/jules/mindos"
