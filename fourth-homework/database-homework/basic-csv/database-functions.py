from os import path
import csv


def confirm_overwrite(filename):
    response = input(
        f"{filename} already exists and will be overwritten! Are you sure you want to continue? (y/n): "
    )
    return response.lower() == "y"


def init_db(filename, headers):
    if path.exists(filename):
        if not confirm_overwrite(filename):
            print("No changes made to the db")

    if not filename.endswith(".csv"):
        print("File must end with .csv")
        return

    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)


def add_record(filename, record):
    with open(filename, "r", encoding="utf-8") as f:
        first_line = f.readline()

    header = first_line.strip().split(",")

    new_row = []
    for column_name in header:
        new_row.append(record.get(column_name, ""))

    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(new_row)


def view_records(filename):
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


def search_record(filename, field, value):
    with open(filename, "r", encoding="utf-8") as f:
        header = f.readline().strip().split(",")
        print()

        if field not in header:
            print(f"The field provided: {field} does not exist in the db.")
            return

        column_number = header.index(field)

        found = False
        row_number = 1

        reader = csv.reader(f)
        for row in reader:
            if row[column_number] == value:
                print(
                    f"Value {value} found on row {row_number}: {header[0]}: {row[0]}, {header[1]}: {row[1]}, {header[2]}: {row[2]}"
                )
                found = True
            row_number += 1

        if not found:
            print(f"No records found with field: {field} and value: {value}")


def delete_record(filename, field, value):
    remaining_rows = []
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)

        if field not in header:
            print(f"The field provided: {field} does not exist in the db.")
            return

        column_number = header.index(field)

        deleted_rows = 0
        for row in reader:
            if row[column_number] == value:
                deleted_rows += 1
            else:
                remaining_rows.append(row)

        with open(filename, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(remaining_rows)

        print(f"Deleted {deleted_rows} records")


# init_db("db.csv", ["Id", "Name", "Email"])
# add_record("db.csv", {"Id": 3, "Name": "vlad", "Email": "vlad@email.com"})
# view_records("db.csv")

search_record("db.csv", "Name", "vlad")
delete_record("db.csv", "Email", "vlad@test.com")
