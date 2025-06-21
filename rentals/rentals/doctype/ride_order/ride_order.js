// Copyright (c) 2025, yousef and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
    refresh(frm, cdt, cdn) {
        if (!frm.is_new()) {
            if (frm.doc.status !== "Accepted")
                frm.add_custom_button("Accept", () => {
                    frm.set_value("status", "Accepted");
                    frm.save()
                }, __("Action"));
            if (frm.doc.status !== "Rejected")
                frm.add_custom_button("Rejected", () => {
                    frm.set_value("status", "Rejected");
                    frm.save()
                }, __("Action"))
        }

    },
});
