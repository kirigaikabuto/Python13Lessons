from .animal import Animal

class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_number(self):
        print(self.getNumber())
