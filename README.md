# AutoTrackr

**AutoTrackr** is a local Python application for tracking vehicle maintenance records. With both a simple command-line interface and a modern GUI built using `customtkinter`, AutoTrackr makes it easy to log, view, and manage service history for multiple vehicles.

## Features

- Add and manage multiple vehicles
- Log maintenance events including:
  - Service type
  - Date
  - Mileage at service
  - Cost
  - Notes
- Edit or delete vehicle and maintenance records
- Scrollable maintenance history display per vehicle
- GUI built with `customtkinter`
- Data is saved locally in a `car_data.json` file

## Requirements

- Python 3.8 or newer
- [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter)

Install the dependency via pip:

pip install customtkinter

## Running the Application
GUI Version

Launch the graphical version of AutoTrackr:

python tkinterFrontend.py

You’ll see a clean interface for managing vehicles and maintenance records.

## CLI Version

To use the terminal-based version:

python main.py

The command-line mode uses a simple numbered menu to perform the same operations.

## File Overview

AutoTrackr/
├── tkinterFrontend.py        # Main GUI application
├── main.py                   # Command-line backend logic and data storage
├── custom_dialogs.py         # Reusable GUI input dialog with prefill/edit support
├── vehicle_dialog.py         # Dialogs for adding vehicles and maintenance records
├── car_data.json             # JSON file storing all vehicle/maintenance data

## Example Data Format

All vehicle and maintenance data is stored in car_data.json:

{
  "vehicles": [
    {
      "id": 1,
      "make": "Honda",
      "model": "Civic",
      "year": "2018",
      "mileage": "76000",
      "maintenance": [
        {
          "service_type": "Tire Rotation",
          "date": "2025-06-15",
          "mileage": "75500",
          "cost": "30",
          "notes": "Rotated front to back"
        }
      ]
    }
  ]
}

## Planned Improvements (Ideas)

    Export data to CSV or PDF

    Reminder system for scheduled maintenance

    VIN lookup and auto-fill

    Tagging or categorizing services

    Dark/light theme toggle and customization
