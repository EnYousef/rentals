# Copyright (c) 2025, yousef and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Driver(Document):
	def set_full_name(self):
		self.full_name = f"{self.first_name}{' ' + self.last_name if self.last_name and self.last_name.strip() != '' else ''}"

	def before_save(self):
		self.set_full_name()
