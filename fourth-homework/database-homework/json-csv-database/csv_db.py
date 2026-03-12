import csv
from utils import confirm_overwrite


def load_csv_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        reader = list(csv.reader(f))
    header = reader[0]
    records = reader[1:]
    return header, records


def save_csv_file(filename, header, records):
    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(records)


def init_csv_db(filename, headers):
    if not confirm_overwrite(filename):
        print("No changes made to the db")
        return

    if "id" in headers:
        headers.remove("id")
    headers.insert(0, "id")

    save_csv_file(filename, headers, [])
    print(f"Database initialized: {filename}")


def add_csv_record(filename, record):
    header, records = load_csv_file(filename)

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
    print(f"Record added with ID: {next_id}")


def view_csv_records(filename):
    header, records = load_csv_file(filename)
    print("Headers:", header)
    for row in records:
        print(row)


def search_csv_record(filename, field, value):
    header, records = load_csv_file(filename)

    if field not in header:
        print("Field not found")
        return

    index = header.index(field)
    found = False

    for row in records:
        if row[index] == str(value):
            print("Found record:", row)
            found = True

    if not found:
        print("No records found.")


def update_csv_record(filename, search_field, search_value, update_field, update_value):
    header, records = load_csv_file(filename)

    if search_field not in header:
        print(f"Field '{search_field}' not found in headers.")
        return

    if update_field not in header or update_field == "id":
        print(f"Cannot update field '{update_field}'")

    search_index = header.index(search_field)
    update_index = header.index(update_field)
    updated = False

    for row in records:
        if row[search_index] == search_value:
            row[update_index] = update_value
        updated = True

    if updated:
        save_csv_file(filename, header, records)
        print("Record updated successfully.")
    else:
        print("No matching record found to update.")


def delete_csv_record(filename, field, value):
    header, records = load_csv_file(filename)

    if field not in header:
        print("Field not found")
        return

    index = header.index(field)
    rows_to_keep = []
    for row in records:
        if row[index] != str(value):
            rows_to_keep.append(row)

    deleted_count = len(records) - len(rows_to_keep)
    save_csv_file(filename, header, rows_to_keep)
    print(f"Deleted {deleted_count} records.")


def get_csv_schema(filename):
    header, _ = load_csv_file(filename)
    return header
