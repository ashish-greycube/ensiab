# -*- coding: utf-8 -*-
# Copyright (c) 2020, GreyCube Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class CustomerFeedbackCT(Document):
	pass

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def get_contacts_for_customer(doctype, txt, searchfield, start, page_len, filters):
	return frappe.db.sql("""select parent from `tabDynamic Link` where parenttype='Contact' 
	and parentfield='links'
and link_doctype='Customer'
and link_name=%s""",(filters["customer"]), as_list=1)	
