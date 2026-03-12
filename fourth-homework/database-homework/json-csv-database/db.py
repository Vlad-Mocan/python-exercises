from os import path

from json_db import (
    init_json_db,
    add_json_record,
    view_json_records,
    search_json_record,
    update_json_record,
    delete_json_record,
    get_json_schema,
)

from csv_db import (
    init_csv_db,
    add_csv_record,
    view_csv_records,
    search_csv_record,
    update_csv_record,
    delete_csv_record,
    get_csv_schema,
)


def get_extension(filename):
    return path.splitext(filename)[1].lower()


def init_db(filename, headers):
    ext = get_extension(filename)
    if ext == ".json":
        init_json_db(filename, headers)
    elif ext == ".csv":
        init_csv_db(filename, headers)
    else:
        print("Unsupported file format.")


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


def update_record(filename, search_field, search_value, update_field, update_value):
    ext = get_extension(filename)
    if ext == ".json":
        update_json_record(
            filename, search_field, search_value, update_field, update_value
        )
    elif ext == ".csv":
        update_csv_record(
            filename, search_field, search_value, update_field, update_value
        )


def delete_record(filename, field, value):
    ext = get_extension(filename)
    if ext == ".json":
        delete_json_record(filename, field, value)
    elif ext == ".csv":
        delete_csv_record(filename, field, value)


def get_schema(filename):
    ext = get_extension(filename)
    if ext == ".json":
        return get_json_schema(filename)
    elif ext == ".csv":
        return get_csv_schema(filename)
