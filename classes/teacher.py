from user import User


class Teacher(User):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
