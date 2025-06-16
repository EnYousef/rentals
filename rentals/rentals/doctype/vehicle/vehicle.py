# Copyright (c) 2025, yousef and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Vehicle(Document):
	def before_save(self):
		self.set_title()

	def set_title(self):
		self.title = f"{self.make} {self.model}, {self.year}"
