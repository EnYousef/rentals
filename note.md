```markdown
## Set Field Value in Frappe

Use the following code to **clear the "amount" field** for a specific document:

```javascript
frm.model.set_value(cdt, cdn, "amount", "");
```

- `cdt`: Child DocType
- `cdn`: Child DocName
- `"amount"`: Field to update
- `""`: New value (empty string)

- `cdt` - `cdn`: can be get after frm in form actin like param of function
--------------------------------
To display a simple alert in Frappe, use:

```javascript
frappe.show_alert("message content");
```

--------------------------------
Stander Url for API

```
http://irfan.cabs:8000/api/v2/document/DocTypeName
```
---------
Access methods as API
```
http://irfan.cabs:8000/api/v2/method/path_of_method
```
---------------------------------
Advance of get all
```python
frappe.get_all("Ride Booking", fields=["vehicle.make", "count(1) as cars_count",  "sum(total_amount) as total_revenue"], filters={"docstatus":"1"}, group_by="make")
// result => [{'make': 'BMW', 'cars_count': 2, 'total_revenue': 200.0}]
```

```python
frappe.get_all("Ride Booking", fields=["vehicle.make", "count(1) as cars_count",  "sum(total_amount) as total_revenue"], filters={"docstatus":">=1"}, group_by="make")
// result => [{'make': 'BMW', 'cars_count': 2, 'total_revenue': 200.0}]
```