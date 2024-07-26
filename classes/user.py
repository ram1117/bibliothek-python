import random


class User:
    rentals = []

    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.userid = random.randint(0, 1000)
        self.role = role

    def add_rental(self, rental):
        if any(rental not in self.rentals):
            self.rentals.append(rental)

    def __str__(self) -> str:
        return f"{self.userid}\t{self.name}\t{self.role}\t{self.age}"
