# Copyright (c) 2025, yousef and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RideBooking(Document):
	def validate(self):
		self.total_amount = 0
		rate = frappe.get_single_value("Rental Settings", "stander_rate")
		total_distance = sum(item.distance for item in self.items)
		self.total_amount = total_distance * rate
