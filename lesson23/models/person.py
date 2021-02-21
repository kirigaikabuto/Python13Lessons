class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        out = f"Name:{self.name};Age:{self.age}"
        print(out)
