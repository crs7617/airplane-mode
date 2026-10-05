# Copyright (c) 2026, Sairam and contributors
# For license information, please see license.txt

import frappe
import random
import string
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
        
    def before_submit(self):
             if self.status != "Boarded":
                   frappe.throw("Cannot submit ticket unless status is Boarded")

    def before_insert(self):
        self.seat = f"{random.randint(1, 99)}{random.choice(string.ascii_uppercase[:5])}"

        def validate(self):
        self.remove_duplicate_addons()
        self.calculate_total_amount()
        self.check_overbooking()

    def check_overbooking(self):
        if not self.flight:
            return
        airplane = frappe.db.get_value("Airplane Flight", self.flight, "airplane")
        capacity = frappe.db.get_value("Airplane", airplane, "capacity")
        existing = frappe.db.count(
            "Airplane Ticket",
            {"flight": self.flight, "name": ["!=", self.name or ""]}
        )
        if existing >= capacity:
            frappe.throw(f"Cannot book more tickets — capacity ({capacity}) reached for this flight.")