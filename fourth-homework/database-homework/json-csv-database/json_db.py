import json
from utils import confirm_overwrite


def load_json_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json_file(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def init_json_db(filename, headers):
    if not confirm_overwrite(filename):
        print("No changes made to the db")
        return

    if "id" in headers:
        headers.remove("id")
    headers.insert(0, "id")

    data = {"schema": headers, "records": []}
    save_json_file(filename, data)
    print(f"Database initialized: {filename}")


def add_json_record(filename, record):
    data = load_json_file(filename)

    if not data["records"]:
        next_id = 1
    else:
        last_id = data["records"][-1].get("id", 0)
        next_id = int(last_id) + 1

    new_entry = {"id": next_id}
    for col in data["schema"]:
        if col == "id":
            continue
        new_entry[col] = record.get(col, "")

    data["records"].append(new_entry)
    save_json_file(filename, data)
    print(f"Record added with ID: {next_id}")


def view_json_records(filename):
    data = load_json_file(filename)
    print("Headers:", data["schema"])
    for record in data["records"]:
        print(list(record.values()))


def search_json_record(filename, field, value):
    data = load_json_file(filename)
    found = False

    for record in data["records"]:
        if str(record.get(field)) == str(value):
            print("Found:", record)
            found = True

    if not found:
        print("No records found.")


def update_json_record(
    filename, search_field, search_value, update_field, update_value
):
    data = load_json_file(filename)

    if update_field not in data["schema"] or update_field == "id":
        print(f"Cannot update field '{update_field}'")
        return

    updated = False

    for record in data["records"]:
        if record.get(search_field) == search_value:
            record[update_field] = update_value
            updated = True

    if updated:
        save_json_file(filename, data)
        print("Record updated successfully.")
    else:
        print("No matching record found.")


def delete_json_record(filename, field, value):
    data = load_json_file(filename)
    original_list = data["records"]
    new_list = []

    for record in original_list:
        if str(record.get(field)) != str(value):
            new_list.append(record)

    deleted_count = len(original_list) - len(new_list)
    data["records"] = new_list
    save_json_file(filename, data)
    print(f"Deleted {deleted_count} records.")


def get_json_schema(filename):
    data = load_json_file(filename)
    return data["schema"]
