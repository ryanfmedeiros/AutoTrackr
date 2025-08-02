import customtkinter as ctk

class AddVehicleDialog(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add New Vehicle")
        self.geometry("400x300")
        self.resizable(False, False)
        self.wait_visibility()
        self.grab_set()
        self.result = None

        ctk.CTkLabel(self, text="Enter Vehicle Information", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(10, 5))

        self.make_entry = self._add_labeled_entry("Make")
        self.model_entry = self._add_labeled_entry("Model")
        self.year_entry = self._add_labeled_entry("Year")
        self.mileage_entry = self._add_labeled_entry("Mileage")

        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(pady=10)

        ctk.CTkButton(btn_frame, text="Add", command=self.on_submit, width=100).pack(side="left", padx=10)
        ctk.CTkButton(btn_frame, text="Cancel", command=self.destroy, width=100).pack(side="left", padx=10)

    def _add_labeled_entry(self, label_text):
        frame = ctk.CTkFrame(self)
        frame.pack(fill="x", padx=20, pady=5)

        label = ctk.CTkLabel(frame, text=label_text, width=70, anchor="w")
        label.pack(side="left")

        entry = ctk.CTkEntry(frame)
        entry.pack(side="left", expand=True, fill="x")
        return entry

    def on_submit(self):
        make = self.make_entry.get()
        model = self.model_entry.get()
        year = self.year_entry.get()
        mileage = self.mileage_entry.get()

        if not all([make, model, year, mileage]):
            ctk.CTkLabel(self, text="All fields are required.", text_color="red").pack()
            return

        self.result = (make, model, year, mileage)
        self.destroy()


def ask_vehicle_info(parent):
    dialog = AddVehicleDialog(parent)
    parent.wait_window(dialog)
    return dialog.result


class AddMaintenanceDialog(ctk.CTkToplevel):
    def __init__(self, parent, vehicle):
        super().__init__(parent)
        self.title("Add Maintenance Record")
        self.geometry("400x360")
        self.resizable(False, False)
        self.wait_visibility()
        self.grab_set()
        self.result = None

        ctk.CTkLabel(self, text=f"Add Maintenance for:\n{vehicle['year']} {vehicle['make']} {vehicle['model']}",
                     font=ctk.CTkFont(size=15, weight="bold"), justify="center").pack(pady=(10, 10))

        self.service_entry = self._add_labeled_entry("Service Type")
        self.date_entry = self._add_labeled_entry("Date (YYYY-MM-DD)")
        self.mileage_entry = self._add_labeled_entry("Mileage at Service")
        self.cost_entry = self._add_labeled_entry("Cost")
        self.notes_entry = self._add_labeled_entry("Notes")

        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(pady=10)

        ctk.CTkButton(btn_frame, text="Add", command=self.on_submit, width=100).pack(side="left", padx=10)
        ctk.CTkButton(btn_frame, text="Cancel", command=self.destroy, width=100).pack(side="left", padx=10)

    def _add_labeled_entry(self, label_text):
        frame = ctk.CTkFrame(self)
        frame.pack(fill="x", padx=20, pady=5)

        label = ctk.CTkLabel(frame, text=label_text, width=120, anchor="w")
        label.pack(side="left")

        entry = ctk.CTkEntry(frame)
        entry.pack(side="left", expand=True, fill="x")
        return entry

    def on_submit(self):
        service_type = self.service_entry.get()
        date = self.date_entry.get()
        mileage = self.mileage_entry.get()
        cost = self.cost_entry.get()
        notes = self.notes_entry.get()

        if not all([service_type, date, mileage, cost]):
            ctk.CTkLabel(self, text="All fields except 'Notes' are required.", text_color="red").pack()
            return

        self.result = {
            "service_type": service_type,
            "date": date,
            "mileage": mileage,
            "cost": cost,
            "notes": notes
        }
        self.destroy()


def ask_maintenance_info(parent, vehicle):
    dialog = AddMaintenanceDialog(parent, vehicle)
    parent.wait_window(dialog)
    return dialog.result


# New EditMaintenanceDialog with prefilled data and single form for editing
class EditMaintenanceDialog(ctk.CTkToplevel):
    def __init__(self, parent, maintenance):
        super().__init__(parent)
        self.title("Edit Maintenance Record")
        self.geometry("400x360")
        self.resizable(False, False)
        self.wait_visibility()
        self.grab_set()
        self.result = None

        ctk.CTkLabel(self, text="Edit Maintenance Record", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(10, 10))

        self.service_entry = self._add_labeled_entry("Service Type", maintenance["service_type"])
        self.date_entry = self._add_labeled_entry("Date (YYYY-MM-DD)", maintenance["date"])
        self.mileage_entry = self._add_labeled_entry("Mileage at Service", maintenance["mileage"])
        self.cost_entry = self._add_labeled_entry("Cost", maintenance["cost"])
        self.notes_entry = self._add_labeled_entry("Notes", maintenance["notes"])

        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(pady=10)

        ctk.CTkButton(btn_frame, text="Save", command=self.on_submit, width=100).pack(side="left", padx=10)
        ctk.CTkButton(btn_frame, text="Cancel", command=self.destroy, width=100).pack(side="left", padx=10)

    def _add_labeled_entry(self, label_text, initial_value=""):
        frame = ctk.CTkFrame(self)
        frame.pack(fill="x", padx=20, pady=5)

        label = ctk.CTkLabel(frame, text=label_text, width=120, anchor="w")
        label.pack(side="left")

        entry = ctk.CTkEntry(frame)
        entry.pack(side="left", expand=True, fill="x")
        entry.insert(0, initial_value)
        return entry

    def on_submit(self):
        service_type = self.service_entry.get()
        date = self.date_entry.get()
        mileage = self.mileage_entry.get()
        cost = self.cost_entry.get()
        notes = self.notes_entry.get()

        if not all([service_type, date, mileage, cost]):
            ctk.CTkLabel(self, text="All fields except 'Notes' are required.", text_color="red").pack()
            return

        self.result = {
            "service_type": service_type,
            "date": date,
            "mileage": mileage,
            "cost": cost,
            "notes": notes
        }
        self.destroy()


def ask_edit_maintenance_info(parent, maintenance):
    dialog = EditMaintenanceDialog(parent, maintenance)
    parent.wait_window(dialog)
    return dialog.result
