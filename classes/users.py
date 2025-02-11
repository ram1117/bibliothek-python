import utils.fileutil as fileutil
from utils.validateinput import validate_empty_input
from classes.student import Student
from classes.teacher import Teacher
from pathlib import Path
import os

filepath = Path(os.getcwd()) / "data" / "user.json"


class Users:

    def __init__(self):
        self.users = fileutil.read_from_file(filepath) or []

    def list_users(self):
        if len(self.users) == 0:
            print("******* No Users found *******")
            return
        print("******* Users *******\n")
        for x in self.users:
            print(str(x))

    def add_user(self):
        print("Do you want to add [1]Student [2]Staff\n")
        usertype = input("Enter Option:\n")

        if usertype == "1":
            self.add_student()
        elif usertype == "2":
            self.add_teacher()
        else:
            print("Enter valid option")

    def add_student(self):
        name = validate_empty_input("Name")
        age = validate_empty_input("Age")
        classroom = validate_empty_input("ClassRoom")
        student = Student(name, age, classroom)
        self.users.append(student)
        fileutil.write_to_file(filepath, self.users)
        return

    def add_teacher(self):
        name = validate_empty_input("Name:")
        age = validate_empty_input("Age:")
        subject = validate_empty_input("Subject:")
        teacher = Teacher(name, age, subject)
        self.users.append(teacher)
        fileutil.write_to_file(filepath, self.users)
        return
