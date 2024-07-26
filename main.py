import applists.users as usersEntity

users = usersEntity.Users()
menu_options = {"1": "", "2": users.list_users}
main_menu = (
    "\nPlease choose an option:\n1.List all books\n2.List all people\n3.Create a person\n4.Create a book\n"
    "5.Create a rental\n6.List all rentals for a given Person ID\n7.Exit\n\n"
)


def start_app():
    while main_menu:
        print(main_menu)
        input_option = input("Enter option: \n")
        if input_option == "7":
            break
        menu_options[input_option]()


start_app()
