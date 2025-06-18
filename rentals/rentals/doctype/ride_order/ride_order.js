// Copyright (c) 2025, yousef and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
    refresh(frm) {
        if (!frm.is_new() && frm.doc.status !== "Accepted")
            frm.add_custom_button("Accept", () => {
                frm.set_value("status", "Accepted");
                frm.save()
            });
    },
});
