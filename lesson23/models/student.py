class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def print_info(self):
        out = f"Name:{self.name};Age:{self.age};Grade:{self.grade.get_info()}"
        print(out)
