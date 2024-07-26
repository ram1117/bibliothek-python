from classes.book import Book
from utils.validateinput import validate_empty_input


class Books:
    def __init__(self):
        self.books = []

    def add_book(self):
        booktitle = validate_empty_input("Book Title")
        book = Book(booktitle)
        self.books.append(book)

    def list_books(self):
        if len(self.books) == 0:
            print("******* No books found *******")
            return
        print("******* Books *******\n")
        for x in self.books:
            print(str(x))
