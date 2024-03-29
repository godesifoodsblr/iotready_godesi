from . import __version__ as app_version

app_name = "iotready_godesi"
app_title = "IoTReady Go Desi"
app_publisher = "IoTReady"
app_description = "IoTReady Custom App For Go Desi"
app_email = "hello@iotready.co"
app_license = "UNLICENSED"
required_apps = ["erpnext"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/iotready_godesi/css/iotready_godesi.css"
# app_include_js = "/assets/iotready_godesi/js/iotready_godesi.js"

# include js, css files in header of web template
# web_include_css = "/assets/iotready_godesi/css/iotready_godesi.css"
# web_include_js = "/assets/iotready_godesi/js/iotready_godesi.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "iotready_godesi/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "iotready_godesi.utils.jinja_methods",
# 	"filters": "iotready_godesi.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "iotready_godesi.install.before_install"
# after_install = "iotready_godesi.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "iotready_godesi.uninstall.before_uninstall"
# after_uninstall = "iotready_godesi.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "iotready_godesi.notifications.get_notification_config"

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

doc_events = {
    "Warehouse": {"before_save": "iotready_godesi.doc_hooks.warehouse_before_save"},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"iotready_godesi.tasks.all"
# 	],
# 	"daily": [
# 		"iotready_godesi.tasks.daily"
# 	],
# 	"hourly": [
# 		"iotready_godesi.tasks.hourly"
# 	],
# 	"weekly": [
# 		"iotready_godesi.tasks.weekly"
# 	],
# 	"monthly": [
# 		"iotready_godesi.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "iotready_godesi.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "iotready_godesi.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "iotready_godesi.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"iotready_godesi.auth.validate"
# ]
