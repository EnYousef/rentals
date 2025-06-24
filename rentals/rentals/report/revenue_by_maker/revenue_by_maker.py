# Copyright (c) 2025, yousef and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [], []
	# Logging In Frappe
	# frappe.errprint("---" * 20)
	# frappe.errprint(filters)
	data = frappe.get_all(
		"Ride Booking",
		fields=["vehicle.make", "count(1) as cars_count", "sum(total_amount) as total_revenue"],
		filters={"docstatus": "1"},
		group_by="make",
	)
	columns = [
		{"fieldname": "make", "fieldlable": "Make", "fieldtype": "Data"},
		{
			"fieldname": "total_revenue",
			"fieldlable": "Total Revenue",
			"fieldtype": "Currency",
			"option": "YER",
		},
	]
	chart = {
		"data": {
			"labels": [val.make for val in data],
			"datasets": [{"values": [val.total_revenue for val in data]}],
		},
		"type": "donut",
	}
	return columns, data, "This is The Report", chart
