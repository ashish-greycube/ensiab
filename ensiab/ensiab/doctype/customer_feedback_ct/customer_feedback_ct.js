// Copyright (c) 2020, GreyCube Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Customer Feedback CT', {
	setup: function(frm) {
		frm.set_query('sales_invoice', () => {
			return {
				filters: {
					customer: frm.doc.customer
				}
			}
		})
		frm.set_query('contact_person', () => {
			return {
				query: 'ensiab.ensiab.doctype.customer_feedback_ct.customer_feedback_ct.get_contacts_for_customer',
				filters: {
					'customer': frm.doc.customer
				}
			}
		})			
	},
	customer: function(frm) {
		frm.set_value('sales_invoice', '')
		frm.set_value('contact_person', '')
		frm.set_value('mobile', '')
		frm.set_value('whatsapp_no', '')
		frm.set_value('email', '')
	}
});
