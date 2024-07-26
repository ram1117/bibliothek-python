import random


class Book:
    def __init__(self, title) -> None:
        self.id = random.randint(0, 1000)
        self.title = title

    def __str__(self) -> str:
        return f"{self.id}\t{self.title}"
