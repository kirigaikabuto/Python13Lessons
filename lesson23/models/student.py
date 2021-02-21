from .person import Person


class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name=name, age=age)
        self.grade = grade

    def print_info(self):
        out = super().get_info() + f"Grade:{self.grade.get_info()}"
        print(out)
