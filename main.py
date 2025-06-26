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

def add_vehicle(data):
    make = input("Make: ")
    model = input("Model: ")
    year = input("Year: ")
    mileage = input("Mileage: ")
    vehicle = {
        "id": len(data["vehicles"]) + 1,
        "make": make,
        "model": model,
        "year": year,
        "mileage": mileage,
        "maintenance": []
    }
    data["vehicles"].append(vehicle)
    print("Vehicle added!")

def add_maintenance(data):
    if not data["vehicles"]:
        print("No vehicles found, add one first.")
        return
    for v in data["vehicles"]:
        print(f'{v["id"]}: {v["year"]} {v["make"]} {v["model"]}')
    vehicle_id = int(input("Select vehicle ID for maintenance: "))
    vehicle = next((v for v in data["vehicles"] if v["id"] == vehicle_id), None)
    if not vehicle:
        print("Invalid vehicle ID")
        return
    service_type = input("Service Type (e.g., Oil Change): ")
    date = input("Date (YYYY-MM-DD): ")
    mileage = input("Mileage at service: ")
    cost = input("Cost: ")
    notes = input("Notes: ")
    maintenance = {
        "service_type": service_type,
        "date": date,
        "mileage": mileage,
        "cost": cost,
        "notes": notes
    }
    vehicle["maintenance"].append(maintenance)
    print("Maintenance record added!")

def view_vehicles(data):
    if not data["vehicles"]:
        print("No vehicles added yet.")
        return
    for v in data["vehicles"]:
        print(f'ID: {v["id"]}, {v["year"]} {v["make"]} {v["model"]}, Mileage: {v["mileage"]}')
        if v["maintenance"]:
            print("  Maintenance:")
            for m in v["maintenance"]:
                print(f'    - {m["date"]}: {m["service_type"]} at {m["mileage"]} miles, Cost: {m["cost"]}')
        else:
            print("  No maintenance records.")

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
            add_vehicle(data)
        elif choice == '2':
            add_maintenance(data)
        elif choice == '3':
            view_vehicles(data)
        elif choice == '4':
            save_data(data)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
