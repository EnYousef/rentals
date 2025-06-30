import asyncio

import frappe
import frappe.push_notification


@frappe.whitelist()
def get_text():
	return "Welcome There!"


def throw_text(doc, event):
	frappe.throw("Is run now!")


async def schedular_mth():
	print("FBBBBBBBBBBBBBBBBBBBBBBBBBBB")
	send_notifications()
	for i in range(60):
		print(f"Second {i + 1}")
		await asyncio.sleep(1)


# /path/to/your/app/[app_name]/[app_name]/server_scripts/send_notifications.py


def send_notifications():
	users = frappe.get_all("User", fields=["name"])

	for user in users:
		frappe.publish_realtime(
			event="msgprint", message="This is your scheduled notification", user=user.name
		)

		# Alternative: Create Notification Log entry
		frappe.get_doc(
			{
				"doctype": "Notification Log",
				"subject": f"Scheduled Notification {user.name} تبا لك ي ادهم",
				"for_user": user.name,
				"type": "Alert",
				"email_content": "This is your scheduled notification",
			}
		).insert(ignore_permissions=True)


def test_enq():
	"""
	How Run:
		frappe.enqueue("rentals.api.test_enq", "short")
	"""
	pass
