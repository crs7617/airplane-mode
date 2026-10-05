# Copyright (c) 2026, Sairam and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns = [
        {"label": "Airline", "fieldname": "airline", "fieldtype": "Link", "options": "Airline", "width": 200},
        {"label": "Revenue", "fieldname": "revenue", "fieldtype": "Currency", "width": 150},
    ]

    Airline = frappe.qb.DocType("Airline")
    Airplane = frappe.qb.DocType("Airplane")
    Flight = frappe.qb.DocType("Airplane Flight")
    Ticket = frappe.qb.DocType("Airplane Ticket")

    query = (
        frappe.qb.from_(Airline)
        .left_join(Airplane).on(Airplane.airline == Airline.name)
        .left_join(Flight).on(Flight.airplane == Airplane.name)
        .left_join(Ticket).on((Ticket.flight == Flight.name) & (Ticket.docstatus == 1))
        .select(Airline.name.as_("airline"), frappe.qb.functions.Sum(Ticket.total_amount).as_("revenue"))
        .groupby(Airline.name)
    )
    data = query.run(as_dict=True)
    for row in data:
        row.revenue = row.revenue or 0

    chart = {
        "data": {
            "labels": [r["airline"] for r in data],
            "datasets": [{"values": [r["revenue"] for r in data]}],
        },
        "type": "donut",
    }
    report_summary = [{"value": sum(r["revenue"] for r in data), "label": "Total Revenue", "datatype": "Currency"}]

    return columns, data, None, chart, report_summary