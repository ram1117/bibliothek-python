from classes.users import Users
from classes.books import Books
from classes.rentals import Rentals

users = Users()
books = Books()
rentals = Rentals(books.books, users.users)
menu_action = {
    "1": books.list_books,
    "2": users.list_users,
    "3": users.add_user,
    "4": books.add_book,
    "5": rentals.create_rental,
    "6": rentals.list_rentals,
}
main_menu = (
    "\nPlease choose an option:\n1.List all books\n2.List all people\n3.Create a person\n4.Create a book\n"
    "5.Create a rental\n6.List all rentals\n7.Exit\n\n"
)


def start_app():
    while main_menu:
        print(main_menu)
        input_option = input("Enter option: \n")
        if input_option == "7":
            break
        menu_action[input_option]()


start_app()
