from model.entity import Entity
from model.impl.book import Book
from model.impl.user import User


class UserBook(Entity):
    id_user: int
    id_book: int

    user_db: User
    book_db: Book

    def __init__(self, user_db, book_db):
        self.user_db = user_db
        self.book_db = book_db
        super().__init__("user_book.csv", ["id_user", "id_book"])

    def add(self, id_user: int, id_book: int):
        if str(id_book) in self.get_user_book_ids(id_user):
            print("Could not add book, user already selected")
            return

        values = [id_user, id_book]
        super().add(values)

    def get_user_book_ids(self, id_user):
        records = self.get("id_user", str(id_user))
        if not records:
            return []

        return [record[2] for record in records]

    def get_books(self, id_user):
        books = []
        book_ids = self.get_user_book_ids(id_user)

        if book_ids:
            for book_id in book_ids:
                books.append(self.book_db.get("id", book_id))

        return books

    def has_read_book(self, id_user, id_book):
        book_ids = self.get_user_book_ids(id_user)

        if book_ids:
            for book_id in book_ids:
                if int(book_id) == int(id_book):
                    return True

        return False

    def remove_book(self, user_id, book_id):
        if not self.has_read_book(str(user_id), str(book_id)):
            print("Could not remove book, it doesn't exist for the user")
            return

        # values = self.list()
        values_to_keep = []

        if values:
            for value in values:
                if value[1] != str(user_id) and value[2] != str(book_id):
                    # values_to_keep = values_to_keep.append(value)
        print(values)
