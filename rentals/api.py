import frappe


@frappe.whitelist()
def get_text():
	return "Welcome There!"


def throw_text(doc, event):
	frappe.throw("Is run now!")
