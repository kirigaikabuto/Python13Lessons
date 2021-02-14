class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_private_info(self):
        print(self.name, self.age)

    def print_info(self):
        print("it is class of animal")

    def getNumber(self):
        return 56
