// Copyright (c) 2025, yousef and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Booking", {
    refresh(frm) {
    },
    update_total_amount(frm) {
        let total = frm.doc.items.map(e => e.distance).reduce((o, n) => o + n, 0) * frm.doc.rate;
        frm.set_value("total_amount", total);
    },
    rate(frm) {
        frm.trigger("update_total_amount");
    }
});


frappe.ui.form.on('Ride Booking Item', {
    refresh(frm) {
        // your code here
    },
    distance(frm, cdt, cdn) {
        frm.trigger("update_total_amount");
    }
})