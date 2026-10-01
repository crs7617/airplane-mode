# Copyright (c) 2026, Sairam and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class AirplaneTicket(Document):
    def validate(self):
        self.remove_duplicate_addons()
        self.calculate_total_amount()

    def remove_duplicate_addons(self):
        seen = set()
        unique_rows = []
        for row in self.add_ons:
            if row.item not in seen:
                seen.add(row.item)
                unique_rows.append(row)
        self.add_ons = unique_rows

    def calculate_total_amount(self):
        addon_total = sum(row.amount or 0 for row in self.add_ons)
        self.total_amount = (self.flight_price or 0) + addon_total