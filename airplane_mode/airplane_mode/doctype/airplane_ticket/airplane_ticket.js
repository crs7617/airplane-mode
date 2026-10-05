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


frappe.ui.form.on('Airplane Ticket', {
	refresh(frm) {
		frm.add_custom_button(__('Assign Seat'), () => {
			let dialog = new frappe.ui.Dialog({
				title: 'Assign Seat',
				fields: [
					{ label: 'Seat Number', fieldname: 'seat_number', fieldtype: 'Data', reqd: 1 }
				],
				primary_action_label: 'Assign',
				primary_action(values) {
					frm.set_value('seat', values.seat_number);
					dialog.hide();
				}
			});
			dialog.show();
		});
	}
});