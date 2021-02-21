from .person import Person


class Employee(Person):

    def __init__(self, name, age, salary):
        super().__init__(name=name, age=age)
        self.salary = salary

    def print_info(self):
        out = super().get_info() + f"Salary:{self.salary}"
        print(out)
