import json
import os
from json_functions import (
    init_json_db,
    add_json_record,
    view_json_records,
    search_json_record,
    delete_json_record,
)

from csv_functions import (
    init_csv_db,
    add_csv_record,
    view_csv_records,
    search_csv_record,
    delete_csv_record,
)


def get_extension(filename):
    return os.path.splitext(filename)[1].lower()


def init_db(filename, headers):
    ext = get_extension(filename)
    if ext == ".json":
        init_json_db(filename, headers)
    elif ext == ".csv":
        init_csv_db(filename, headers)
    else:
        print("Unsupported file format.")
        return
    print(f"Database initialized: {filename}")


def add_record(filename, record):
    ext = get_extension(filename)
    if ext == ".json":
        add_json_record(filename, record)
    elif ext == ".csv":
        add_csv_record(filename, record)


def view_records(filename):
    ext = get_extension(filename)
    if ext == ".json":
        view_json_records(filename)
    elif ext == ".csv":
        view_csv_records(filename)


def search_record(filename, field, value):
    ext = get_extension(filename)
    if ext == ".json":
        search_json_record(filename, field, value)
    elif ext == ".csv":
        search_csv_record(filename, field, value)


def delete_record(filename, field, value):
    ext = get_extension(filename)
    if ext == ".json":
        delete_json_record(filename, field, value)
    elif ext == ".csv":
        delete_csv_record(filename, field, value)


def main():
    print("--- JSON/CSV Database Manager ---")
    filename = input("Enter filename: ").strip()

    while True:
        print(f"\nCurrently managing: {filename}")
        print("1. Initialize DB (New/Overwrite)")
        print("2. Add Record")
        print("3. View All Records")
        print("4. Search Record")
        print("5. Delete Record")
        print("6. Change File")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            h = input("Enter headers separated by commas: ").split(",")
            headers = [item.strip() for item in h]
            init_db(filename, headers)

        elif choice == "2":
            headers = []
            ext = get_extension(filename)

            if ext == ".json":
                with open(filename, "r") as f:
                    headers = json.load(f).get("schema", [])
            elif ext == ".csv":
                with open(filename, "r") as f:
                    headers = f.readline().strip().split(",")

            record = {}
            print(f"Adding record to {filename}:")
            for column in headers:
                val = input(f"Enter value for '{column}': ")
                record[column] = val

            add_record(filename, record)
            print("Record added successfully.")

        elif choice == "3":
            view_records(filename)

        elif choice == "4":
            f = input("Field to search: ")
            v = input("Value to find: ")
            search_record(filename, f, v)

        elif choice == "5":
            f = input("Field to target: ")
            v = input("Value to delete: ")
            delete_record(filename, f, v)

        elif choice == "6":
            filename = input("Enter new filename: ").strip()

        elif choice == "7":
            print("Thank you!")
            break
        else:
            print("Invalid selection.")


main()
