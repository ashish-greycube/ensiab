from __future__ import unicode_literals
from frappe import _
import frappe


def get_data():
    config = [
        {
            "label": _("Tools"),
            "items": [
                {
                    "type": "doctype",
                    "label":"Customer Feedback",
                    "name": "Customer Feedback CT",
                    "description": "Customer Feedback CT"
                }
            ]
        }]
    return config