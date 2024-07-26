import utils.fileutil
from utils.validateinput import validate_empty_input
from classes.student import Student
from classes.teacher import Teacher


class Users:
    users = []

    def __init__(self):
        self.users = self.load_users_from_file()
        print(f"Persons - {self.users}")

    def list_users(self):
        print(self.users)

    def add_user(self):
        print("Do you want to add [1]Staff [2]Student\n")
        usertype = input("Enter Option:\n")
        if usertype == "1":
            self.add_student()
        elif usertype == "2":
            self.add_teacher
        else:
            print("Enter valid option")

    def add_student(self):
        print("Enter name:\n")
        name = validate_empty_input("Name:")
        print("Enter Age:\n")
        age = validate_empty_input("Age:")
        print("Enter Classroom:\n")
        classroom = validate_empty_input("ClassRoom:")
        student = Student(name, age, classroom)
        self.users.append(student)
        return

    def add_teacher(self):
        print("Enter name:\n")
        name = validate_empty_input("Name:")
        print("Enter Age:\n")
        age = validate_empty_input("Age:")
        print("Enter Classroom:\n")
        subject = validate_empty_input("Subject:")
        teacher = Teacher(name, age, subject)
        self.users.append(teacher)
        return

    def load_users_from_file(self):
        return utils.fileutil.read_from_file("../data/users.json")
