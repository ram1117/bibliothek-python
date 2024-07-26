import random


class User:
    rentals = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.userid = random.randint(0, 1000)

    def add_rental(self, rental):
        if any(rental not in self.rentals):
            self.rentals.append(rental)
