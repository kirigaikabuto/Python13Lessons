class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = self.salary

    def print_info(self):
        out = f"Name:{self.name};Age:{self.age};Salary:{self.salary}"
        print(out)
