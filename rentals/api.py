import frappe


@frappe.whitelist()
def get_text():
	return "Welcome There!"
