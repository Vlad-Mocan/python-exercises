from model.entity import Entity


class User(Entity):
    name: str
    email: str

    def add(self, name: str, email: str):
        values = [name, email]
        return super().add(values)
