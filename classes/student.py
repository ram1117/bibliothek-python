from user import User


class Student(User):
    def __init__(self, name, age, classroom):
        super().__init__(name, age)
        self.classroom = classroom
