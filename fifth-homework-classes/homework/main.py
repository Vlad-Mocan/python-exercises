import os
from model.impl.user import User
from model.impl.book import Book
from model.impl.user_book import UserBook


def main():
    user_model = User("user.csv", ["name", "email"])
    book_model = Book("book.json", ["title", "author", "year"])
    user_books_model = UserBook(user_model, book_model)

    users_to_add = [
        ("Alice Smith", "alice@example.com"),
        ("Bob Jones", "bob.jones@techmail.org"),
        ("Charlie Brown", "charlie@peanuts.com"),
    ]

    books_to_add = [
        ("The Hobbit", "J.R.R. Tolkien", 1937),
        ("Foundation", "Isaac Asimov", 1951),
        ("Brave New World", "Aldous Huxley", 1932),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925),
    ]

    if not os.path.exists("user.csv"):
        user_model.initialize_db()
        for name, email in users_to_add:
            user_model.add(name, email)
    if not os.path.exists("book.json"):
        book_model.initialize_db()
        for title, author, year in books_to_add:
            book_model.add(title, author, year)
    if not os.path.exists("user_book.csv"):
        user_books_model.initialize_db()

        alice_id = int(user_model.get("name", "Alice Smith")[0][0])
        bob_id = int(user_model.get("name", "Bob Jones")[0][0])

        hobbit_id = int(book_model.get("title", "The Hobbit")[0]["id"])
        foundation_id = int(book_model.get("title", "Foundation")[0]["id"])
        brave_world_id = int(book_model.get("title", "Brave New World")[0]["id"])

        user_books_model.add(alice_id, hobbit_id)
        user_books_model.add(alice_id, hobbit_id)
        user_books_model.add(alice_id, foundation_id)
        user_books_model.add(bob_id, foundation_id)
        user_books_model.add(bob_id, brave_world_id)

        print(f"Books for Alice (ID {alice_id}):")
        print(user_books_model.get_books(alice_id))

        print(f"\nBooks for Bob (ID {bob_id}):")
        print(user_books_model.get_books(bob_id))

        print(user_books_model.has_read_book(bob_id, foundation_id))
        print(user_books_model.has_read_book(bob_id, hobbit_id))

        print(user_books_model.remove_book(bob_id, foundation_id))


if __name__ == "__main__":
    main()
