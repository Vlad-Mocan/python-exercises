from enum import Enum


class FuelType(Enum):
    PETROL = 1
    DIESEL = 2
    ELECTRIC = 3


class Vehicle:
    brand: str
    year: int

    def __init__(self, brand: str, year: int):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}, Year: {self.year}", end="")


class Car(Vehicle):
    fuel_type: FuelType

    def __init__(self, brand: str, year: int, fuel_type: FuelType):
        super().__init__(brand, year)
        self.fuel_type = fuel_type

    def display_info(self):
        super().display_info()
        print(f", Fuel: {self.fuel_type.name.title()}")
