from .animal import Animal


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
