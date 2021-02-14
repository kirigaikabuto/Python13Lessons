from .animal import Animal


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def print_number(self):
        print(self.getNumber())
