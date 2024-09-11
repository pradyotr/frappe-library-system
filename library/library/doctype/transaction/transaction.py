# Copyright (c) 2024, pradyot and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Transaction(Document):
	def before_submit(self):
		book   = frappe.get_doc("Book", self.book)
		member = frappe.get_doc("Member", self.member)
		
		if self.type == "Issue":
			if frappe.db.exists("Transaction", {'book': self.book, 'member': self.member, 'type': "Issue", "status":"Open", 'docstatus':1}):
				frappe.throw("Cannot issue same book twice at the same time")
				
			if book.available_quantity == 0:
				frappe.throw(book.title + " is not available currently.")
			else:
				if member.outstanding_debt >= 500.0:
					frappe.throw("Debt higher than Rs. 500. Please clear dues first.")
				else:
					book.available_quantity -= 1
					book.save()
		
		elif self.type == "Return":
			issue_doc = frappe.db.get_value("Transaction", {'book': self.book, 'member': self.member, 'type': "Issue", 'status':"Open", 'docstatus':1}, ["name"])
			if not issue_doc:
				frappe.throw("Book must be issued to return.")
			else:
				issue_transaction = frappe.get_doc("Transaction", issue_doc)
				issue_transaction.status = "Closed"
				issue_transaction.save()
				book.available_quantity += 1
				book.save()
