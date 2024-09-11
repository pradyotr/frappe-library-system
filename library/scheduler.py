import frappe
import json

def update_rent():
	print("running")
	all_transactions = frappe.db.get_all("Transaction", filters={'docstatus':1, 'type':"Issue", 'status':"Open"}, fields=["member", "date"])
	daily_rent = frappe.db.get_single_value("Daily Rent", 'daily_rent')
	for entry in all_transactions:
		member = frappe.get_doc("Member", entry["member"])
		member.outstanding_debt = min(member.outstanding_debt + daily_rent, 500)
		member.save()

@frappe.whitelist()
def import_book_data():
	data = json.loads(frappe.request.data)
	for book in data:
		book["doctype"] = "Book"
		doc = frappe.get_doc(book)
		doc.insert()
	
	
