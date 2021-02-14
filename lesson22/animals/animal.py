class Animal:
    def __init__(self, name, age):
        self.nam = name
        self.ag = age

    def get_info(self):
        out = f"Name:{self.nam},Age:{self.ag}"
        return out

    def print_info(self):
        print("it is class of animal")

    def getNumber(self):
        return 56
