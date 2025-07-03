# Copyright (c) 2025, yousef and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestDriver(FrappeTestCase):
	def test_full_name_correctly_set(self):
		test_doc = frappe.new_doc("Driver")
		test_doc.first_name = "Yousef"
		test_doc.first_name = "Khaled"
		test_doc.license_number = "7824B"
		test_doc.save()

		self.assertEqual(test_doc.full_name, "Yousef Khaled")
