import customtkinter as ctk
from tkinter import messagebox
from custom_dialogs import ask_prefill_input
from vehicle_dialog import ask_vehicle_info
from vehicle_dialog import ask_maintenance_info
from vehicle_dialog import ask_edit_maintenance_info
import main  # backend 

class CarMaintenanceApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Car Maintenance Tracker")
        self.geometry("500x450")
        ctk.set_appearance_mode("System")  # "Light", "Dark", or "System"
        ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

        self.data = main.load_data()

        self.create_widgets()

    def create_widgets(self):
        frame = ctk.CTkFrame(self)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        title = ctk.CTkLabel(frame, text="Car Maintenance Tracker", font=ctk.CTkFont(size=20, weight="bold"))
        title.pack(pady=(10, 20))

        ctk.CTkButton(frame, text="➕ Add Vehicle", command=self.add_vehicle).pack(pady=5, fill='x')
        ctk.CTkButton(frame, text="🛠 Add Maintenance Record", command=self.add_maintenance).pack(pady=5, fill='x')
        ctk.CTkButton(frame, text="📋 View Vehicles", command=self.view_vehicles).pack(pady=5, fill='x')
        ctk.CTkButton(frame, text="💾 Save and Exit", command=self.save_and_exit).pack(pady=20, fill='x')

    def add_vehicle(self):
        result = ask_vehicle_info(self)
        if result is None:
            return

        make, model, year, mileage = result
        self.data = main.add_vehicle(self.data, make, model, year, mileage)
        main.save_data(self.data)
        messagebox.showinfo("Success", "Vehicle added!")

    def add_maintenance(self):
        if not self.data["vehicles"]:
            messagebox.showwarning("Warning", "No vehicles found. Add one first.")
            return

        # Popup window to select vehicle
        popup = ctk.CTkToplevel(self)
        popup.title("Select Vehicle")
        popup.geometry("400x300")
        popup.wait_visibility()
        popup.grab_set()

        label = ctk.CTkLabel(popup, text="Select a vehicle to add maintenance:", font=ctk.CTkFont(size=16, weight="bold"))
        label.pack(pady=10)

        frame = ctk.CTkScrollableFrame(popup)
        frame.pack(expand=True, fill="both", padx=10, pady=10)

        for vehicle in self.data["vehicles"]:
            vehicle_text = f'{vehicle["year"]} {vehicle["make"]} {vehicle["model"]} (ID: {vehicle["id"]})'
            btn = ctk.CTkButton(
                frame,
                text=vehicle_text,
                command=lambda v=vehicle: (popup.destroy(), self.open_maintenance_form(v))
            )
            btn.pack(fill="x", pady=5, padx=5)

    def open_maintenance_form(self, vehicle):
        result = ask_maintenance_info(self, vehicle)
        if result is None:
            return

        try:
            self.data = main.add_maintenance(
                self.data,
                vehicle["id"],
                result["service_type"],
                result["date"],
                result["mileage"],
                result["cost"],
                result["notes"]
            )
            main.save_data(self.data)
            messagebox.showinfo("Success", f"Maintenance added for {vehicle['make']} {vehicle['model']}.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def view_vehicles(self):
        if not self.data["vehicles"]:
            messagebox.showinfo("Info", "No vehicles added yet.")
            return

        # Create or reuse popup window for vehicles & maintenance display
        if hasattr(self, 'view_popup') and self.view_popup.winfo_exists():
            self.view_popup.lift()
            return

        self.view_popup = ctk.CTkToplevel(self)
        self.view_popup.title("Vehicles")
        self.view_popup.geometry("500x400")
        self.view_popup.wait_visibility()
        self.view_popup.grab_set()

        self.show_vehicle_list()

    def show_vehicle_list(self):
        """Display list of vehicles with delete and select buttons."""
        for widget in self.view_popup.winfo_children():
            widget.destroy()

        label = ctk.CTkLabel(self.view_popup, text="Select a vehicle to view maintenance or delete:", font=ctk.CTkFont(size=16, weight="bold"))
        label.pack(pady=10)

        frame = ctk.CTkScrollableFrame(self.view_popup)
        frame.pack(expand=True, fill="both", padx=10, pady=10)

        for vehicle in self.data["vehicles"]:
            vehicle_text = f'{vehicle["year"]} {vehicle["make"]} {vehicle["model"]} (ID: {vehicle["id"]})'

            container = ctk.CTkFrame(frame)
            container.pack(fill="x", pady=5, padx=5)

            btn = ctk.CTkButton(
                container,
                text=vehicle_text,
                width=280,
                command=lambda v=vehicle: self.show_vehicle_maintenance(v)
            )
            btn.pack(side="left", padx=(0,10), pady=5)

            del_btn = ctk.CTkButton(
                container,
                text="Delete",
                fg_color="red",
                hover_color="#ff5555",
                width=80,
                command=lambda v=vehicle: self.confirm_delete_vehicle(v)
            )
            del_btn.pack(side="left", pady=5)

    def show_vehicle_maintenance(self, vehicle):
        """Show vehicle info and maintenance records with edit buttons in same window."""
        for widget in self.view_popup.winfo_children():
            widget.destroy()

        header_frame = ctk.CTkFrame(self.view_popup)
        header_frame.pack(fill="x", pady=10, padx=10)

        vehicle_label = ctk.CTkLabel(
            header_frame,
            text=f'{vehicle["year"]} {vehicle["make"]} {vehicle["model"]}',
            font=ctk.CTkFont(size=18, weight="bold")
        )
        vehicle_label.pack(side="left")

        back_btn = ctk.CTkButton(header_frame, text="⬅ Back", width=80, command=self.show_vehicle_list)
        back_btn.pack(side="right")

        maint_frame = ctk.CTkScrollableFrame(self.view_popup)
        maint_frame.pack(expand=True, fill="both", padx=10, pady=10)

        if not vehicle["maintenance"]:
            no_records_label = ctk.CTkLabel(maint_frame, text="No maintenance records.", font=ctk.CTkFont(size=14, slant="italic"))
            no_records_label.pack(pady=20)
            return

        for idx, m in enumerate(vehicle["maintenance"]):
            entry_frame = ctk.CTkFrame(maint_frame, corner_radius=8)
            entry_frame.pack(fill="x", pady=5, padx=5)

            text = (
                f'Service: {m["service_type"]}\n'
                f'Date: {m["date"]}\n'
                f'Mileage: {m["mileage"]}\n'
                f'Cost: ${m["cost"]}\n'
                f'Notes: {m["notes"]}'
            )
            label = ctk.CTkLabel(entry_frame, text=text, justify="left")
            label.pack(side="left", padx=10, pady=5)

            edit_btn = ctk.CTkButton(entry_frame, text="Edit", width=60,
                                     command=lambda v=vehicle, i=idx: self.edit_maintenance_record(v, i))
            edit_btn.pack(side="right", padx=10, pady=5)

    def edit_maintenance_record(self, vehicle, index):
        m = vehicle["maintenance"][index]

        result = ask_edit_maintenance_info(self, m)
        if result is None:
            return

        vehicle["maintenance"][index] = result
        main.save_data(self.data)
        messagebox.showinfo("Success", "Maintenance record updated.")
        self.show_vehicle_maintenance(vehicle)

    def confirm_delete_vehicle(self, vehicle):
        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to DELETE {vehicle['year']} {vehicle['make']} {vehicle['model']}?\nThis action cannot be undone."
        )
        if confirm:
            self.data["vehicles"] = [v for v in self.data["vehicles"] if v["id"] != vehicle["id"]]
            main.save_data(self.data)
            messagebox.showinfo("Deleted", "Vehicle deleted.")
            self.show_vehicle_list()

    def save_and_exit(self):
        main.save_data(self.data)
        messagebox.showinfo("Saved", "Data saved. Goodbye!")
        self.destroy()


if __name__ == "__main__":
    app = CarMaintenanceApp()
    app.mainloop()
