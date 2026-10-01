import random
import string
import frappe

def execute():
    tickets = frappe.get_all(
        "Airplane Ticket",
        filters={"seat": ["in", ["", None]]},
        pluck="name"
    )
    for ticket_name in tickets:
        seat = f"{random.randint(1, 99)}{random.choice(string.ascii_uppercase[:5])}"
        frappe.db.set_value("Airplane Ticket", ticket_name, "seat", seat)
    frappe.db.commit()