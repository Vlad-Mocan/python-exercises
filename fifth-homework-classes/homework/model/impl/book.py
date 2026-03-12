from model.entity import Entity


class Book(Entity):
    title: str
    author: str
    year: int

    def add(self, title: str, author: str, year: int):
        values = [title, author, year]
        super().add(values)
