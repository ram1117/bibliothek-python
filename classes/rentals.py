from classes.rental import Rental
from classes.user import User
from utils.validateinput import validate_empty_input


class Rentals:
    def __init__(self, books, users) -> None:
        self.rentals = []
        self.books = books
        self.users = users

    def create_rental(self):
        for x in self.books:
            print(str(x))
        bookid = int(validate_empty_input("Book Id"))
        for x in self.users:
            print(str(x))
        userid = int(validate_empty_input("User Id"))
        book = self.find_book(bookid)
        if book == None:
            print("Book Not found")
            return

        user = self.find_user(userid)
        if user == None:
            print("User Not found")
            return
        rental = Rental(book, user)
        print(str(rental))
        self.rentals.append(rental)

    def list_rentals(self):
        if len(self.rentals) == 0:
            print("******* No Rentals found *******")
            return
        for x in self.rentals:
            print("******* Rentals *******\n")
            print(str(x))

    def find_book(self, bookid):
        for x in self.books:
            if x.id == bookid:
                return x

    def find_user(self, userid):
        for x in self.users:
            if x.userid == userid:
                return x
