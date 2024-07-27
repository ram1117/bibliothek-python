import utils.fileutil as fileutil
from classes.book import Book
from utils.validateinput import validate_empty_input
from pathlib import Path
import os

filepath = Path(os.getcwd()) / "data" / "books.json"


class Books:
    def __init__(self):
        self.books = fileutil.read_from_file(filepath) or []

    def add_book(self):
        booktitle = validate_empty_input("Book Title")
        book = Book(booktitle)
        self.books.append(book)
        fileutil.write_to_file(filepath, self.books)

    def list_books(self):
        if len(self.books) == 0:
            print("******* No books found *******")
            return
        print("******* Books *******\n")
        for x in self.books:
            print(str(x))
