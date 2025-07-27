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

## GUI Version

Launch the graphical version of AutoTrackr:

py tkinterFrontend.py

You’ll see a clean interface for managing vehicles and maintenance records.

## CLI Version

To use the terminal-based version:

py main.py

The command-line mode uses a simple numbered menu to perform the same operations.

## Planned Improvements (Ideas)

    Export data to CSV or PDF

    Reminder system for scheduled maintenance

    VIN lookup and auto-fill

    Tagging or categorizing services

    Dark/light theme toggle and customization
