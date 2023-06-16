import frappe
from datetime import datetime, timedelta
from iotready_godesi import utils, validations
from frappe.utils import now


def get_picklists():
    """
    Returns a list of picklists for the user's warehouse.
    The list is a list of dictionaries. Each dictionary is guaranteed to have a list of items, a target, docname and a doctype.
    """
    doctype = "Pick List"
    current_timestamp = datetime.strptime(now(), "%Y-%m-%d %H:%M:%S.%f")
    last_date_to_fetch = current_timestamp.date() - timedelta(days=1)
    filters = {
        "reference_type": doctype,
        "creation": [">=", last_date_to_fetch],
        "status": "Open",
    }
    picklists = frappe.get_all("ToDo", filters=filters, fields=["reference_name"])
    picklists = [x["reference_name"] for x in picklists]
    picklists = [frappe.get_doc(doctype, x) for x in picklists]
    picklists = [x.as_dict() for x in picklists]
    return picklists


def get_picklist_summary(picklist_id):
    return frappe.render_template("templates/includes/picklist_summary.html", {"picklist_id": picklist_id})

def get_package_ids(picklist_id):
    package_ids = ["New"] + list({r.package_id for r in frappe.get_all("Crate Activity", filters={
                    "activity": "Picking",
                    "picklist_id": picklist_id,
                }, fields=["package_id"])})
    return package_ids