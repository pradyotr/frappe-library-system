# Copyright (c) 2024, pradyot and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Book(Document):
	
	def before_save(self):
		
		all_issued = frappe.db.count("Transaction", {'book': self.name, 'type': "Issue", 'status': "Open", 'docstatus': 1})
		if all_issued > self.quantity:
			frappe.throw("Total Quantity cannot be lower than books already issued")
