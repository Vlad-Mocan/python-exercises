from db import (
    init_db,
    add_record,
    view_records,
    search_record,
    update_record,
    delete_record,
    get_schema,
)


def main():
    print("JSON/CSV Database Manager")
    filename = input("Enter filename: ").strip()

    while True:
        print(f"\nCurrently managing: {filename}")
        print("1. Initialize DB (New/Overwrite)")
        print("2. Add Record")
        print("3. View All Records")
        print("4. Search Record")
        print("5. Update Record")
        print("6. Delete Record")
        print("7. Change File")
        print("8. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            h = input("Enter headers separated by commas: ").split(",")

            headers = []
            for item in h:
                headers.append(item.strip())

            init_db(filename, headers)

        elif choice == "2":
            headers = get_schema(filename)

            record = {}
            print(f"Adding record to {filename}:")

            for column in headers:
                if column != "id":
                    val = input(f"Enter value for '{column}': ")
                    record[column] = val

            add_record(filename, record)

        elif choice == "3":
            view_records(filename)

        elif choice == "4":
            field = input("Field to search: ")
            value = input("Value to find: ")
            search_record(filename, field, value)

        elif choice == "5":
            search_field = input("Field to search by: ")
            search_value = input("Value to find: ")
            update_field = input("Field to update: ")
            update_value = input("New value: ")

            update_record(
                filename, search_field, search_value, update_field, update_value
            )

        elif choice == "6":
            field = input("Field to target: ")
            value = input("Value to delete: ")
            delete_record(filename, field, value)

        elif choice == "7":
            filename = input("Enter new filename: ").strip()

        elif choice == "8":
            print("Thank you!")
            break

        else:
            print("Invalid selection.")


if __name__ == "__main__":
    main()
