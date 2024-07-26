from . import user


class Teacher(user.User):
    def __init__(self, name, age, subject):
        super().__init__(name, age, "Teacher")
        self.subject = subject

    def __str__(self) -> str:
        return f"{super().__str__()}\t{self.subject}"
