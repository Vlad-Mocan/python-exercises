import csv
import os


def confirm_overwrite(filename):
    response = input(
        f"{filename} already exists and will be overwritten! Are you sure you want to continue? (y/n): "
    )
    return response.lower() == "y"


def init_csv_db(filename, headers):
    if not confirm_overwrite(filename):
        print("No changes made to the db")
        return

    if "id" in headers:
        headers.remove("id")
    headers.insert(0, "id")

    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)


def add_csv_record(filename, record):

    rows = []
    with open(filename, "r", encoding="utf-8") as f:
        reader = list(csv.reader(f))
        header = reader[0]
        records = reader[1:]

    if not records:
        next_id = 1
    else:
        last_id = records[-1][0]
        next_id = int(last_id) + 1

    new_row = []
    for col in header:
        if col == "id":
            new_row.append(next_id)
        else:
            new_row.append(record.get(col, ""))

    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(new_row)


def view_csv_records(filename):
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


def search_csv_record(filename, field, value):
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)

        if field not in header:
            print("Field not found")
            return

        index = header.index(field)
        found = False

        for row in reader:
            if row[index] == str(value):
                print("Found record:", row)
                found = True

        if not found:
            print("No records found.")


def update_csv_record(filename, search_field, search_value, update_data):
    rows = []
    updated = False

    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)

        if search_field not in header:
            print(f"Field '{search_field}' not found in headers.")
            return

        search_index = header.index(search_field)

        for row in reader:
            if row[search_index] == search_value:
                for field, new_val in update_data.items():
                    if field in header:
                        field_index = header.index(field)
                        row[field_index] = new_val
                updated = True
            rows.append(row)

    if updated:
        with open(filename, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(rows)
        print("Record updated successfully.")
    else:
        print("No matching record found to update.")


def delete_csv_record(filename, field, value):
    rows_to_keep = []
    header = []

    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)

        if field not in header:
            print("Field not found")
            return

        index = header.index(field)
        for row in reader:
            if row[index] != str(value):
                rows_to_keep.append(row)

    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows_to_keep)
