import datetime
from classes.book import Book
from classes.user import User


class Rental:
    def __init__(self, book: Book, user: User):
        self.book = book
        self.user = user
        self.date = datetime.date.today()

    def __str__(self) -> str:
        return f"{self.date}\t{self.book.id}\t{self.book.title}\t{self.user.userid}\t{self.user.name}"
