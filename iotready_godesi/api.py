import frappe
from iotready_godesi import picking, webutils, utils


@frappe.whitelist()
def get_picklists():
    return picking.get_picklists()


@frappe.whitelist()
def get_picklist_summary(picklist_id):
    return picking.get_picklist_summary(picklist_id)


@frappe.whitelist()
def submit_activity_form(**kwargs):
    return webutils.record_event(**kwargs)


@frappe.whitelist()
def get_crate_quantity(crate_id):
    return utils.get_crate_quantity(crate_id)


@frappe.whitelist()
def get_package_ids(picklist_id):
    return picking.get_package_ids(picklist_id)


@frappe.whitelist()
def is_picking_complete(picklist_id):
    return picking.is_picking_complete(picklist_id)


@frappe.whitelist()
def mark_as_complete(picklist_id, note):
    return picking.mark_as_complete(picklist_id, note)
