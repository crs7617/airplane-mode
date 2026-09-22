// Copyright (c) 2026, Sairam and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Ticket", {
// 	refresh(frm) {

// 	},
// });

frappe.listview_settings['Airplane Ticket'] = {
    get_indicator: function(doc) {
        var status_colors = {
            "Booked": "gray",
            "Checked-In": "purple",
            "Boarded": "green"
        };
        return [__(doc.status), status_colors[doc.status], "status,=," + doc.status];
    }
};
