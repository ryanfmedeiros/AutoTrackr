import json
import os

DATA_FILE = 'car_data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {"vehicles": []}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def add_vehicle(data, make, model, year, mileage):
    vehicle = {
        "id": len(data["vehicles"]) + 1,
        "make": make,
        "model": model,
        "year": year,
        "mileage": mileage,
        "maintenance": []
    }
    data["vehicles"].append(vehicle)
    return data

def add_maintenance(data, vehicle_id, service_type, date, mileage, cost, notes):
    vehicle = next((v for v in data["vehicles"] if v["id"] == vehicle_id), None)
    if not vehicle:
        raise ValueError(f"Vehicle with ID {vehicle_id} not found.")
    maintenance = {
        "service_type": service_type,
        "date": date,
        "mileage": mileage,
        "cost": cost,
        "notes": notes
    }
    vehicle["maintenance"].append(maintenance)
    return data

def get_vehicles(data):
    # Return a list of vehicle summaries
    return [{
        "id": v["id"],
        "make": v["make"],
        "model": v["model"],
        "year": v["year"],
        "mileage": v["mileage"],
        "maintenance": v["maintenance"]
    } for v in data["vehicles"]]

def get_vehicle_by_id(data, vehicle_id):
    return next((v for v in data["vehicles"] if v["id"] == vehicle_id), None)

# Your existing CLI interface can remain here,
# but calls these refactored functions and handles all user I/O separately.
def main():
    data = load_data()

    while True:
        print("\nOptions:")
        print("1. Add Vehicle")
        print("2. Add Maintenance Record")
        print("3. View Vehicles and Maintenance")
        print("4. Save and Exit")

        choice = input("Select an option: ")
        if choice == '1':
            make = input("Make: ")
            model = input("Model: ")
            year = input("Year: ")
            mileage = input("Mileage: ")
            data = add_vehicle(data, make, model, year, mileage)
            print("Vehicle added!")
        elif choice == '2':
            if not data["vehicles"]:
                print("No vehicles found, add one first.")
                continue
            for v in data["vehicles"]:
                print(f'{v["id"]}: {v["year"]} {v["make"]} {v["model"]}')
            vehicle_id = int(input("Select vehicle ID for maintenance: "))
            vehicle = get_vehicle_by_id(data, vehicle_id)
            if not vehicle:
                print("Invalid vehicle ID")
                continue
            service_type = input("Service Type (e.g., Oil Change): ")
            date = input("Date (YYYY-MM-DD): ")
            mileage = input("Mileage at service: ")
            cost = input("Cost: ")
            notes = input("Notes: ")
            data = add_maintenance(data, vehicle_id, service_type, date, mileage, cost, notes)
            print("Maintenance record added!")
        elif choice == '3':
            if not data["vehicles"]:
                print("No vehicles added yet.")
            else:
                for v in data["vehicles"]:
                    print(f'ID: {v["id"]}, {v["year"]} {v["make"]} {v["model"]}, Mileage: {v["mileage"]}')
                    if v["maintenance"]:
                        print("  Maintenance:")
                        for m in v["maintenance"]:
                            print(f'    - {m["date"]}: {m["service_type"]} at {m["mileage"]} miles, Cost: {m["cost"]}')
                    else:
                        print("  No maintenance records.")
        elif choice == '4':
            save_data(data)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
