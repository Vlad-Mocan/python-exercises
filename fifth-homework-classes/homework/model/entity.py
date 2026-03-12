from database.db import init_db, add_record, search_record, view_records, delete_record


class Entity:
    filename: str
    headers: []

    def __init__(self, filename, headers):
        self.filename = filename
        self.headers = headers

    def get_filename(self):
        return self.filename

    def initialize_db(self):
        init_db(self.filename, self.headers)

    def add(self, values):
        record = {}
        index = 0

        for col in self.headers:
            if col == "id":
                continue
            record[col] = values[index]
            index += 1

        add_record(self.filename, record)

    def get(self, field, value):
        return search_record(self.filename, field, value)

    def list(self):
        view_records(self.filename)

    def delete(self, field, value):
        delete_record(self.filename, field, value)
