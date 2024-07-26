from . import user


class Student(user.User):
    def __init__(self, name, age, classroom):
        super().__init__(name, age, "Student")
        self.classroom = classroom

    def __str__(self) -> str:
        return f"{super().__str__()}\t{self.classroom}"
