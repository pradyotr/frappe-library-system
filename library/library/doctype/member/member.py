# Copyright (c) 2024, pradyot and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Member(Document):
	def validate(self):
		if self.outstanding_debt > 500:
			frappe.throw("Outstanding Debt cannot be more than 500")
