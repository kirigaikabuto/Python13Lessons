class Animal:
    def __init__(self, name, age):
        self.nam = name
        self.ag = age

    def print_private_info(self):
        print(self.nam, self.ag)

    def print_info(self):
        print("it is class of animal")

    def getNumber(self):
        return 56
