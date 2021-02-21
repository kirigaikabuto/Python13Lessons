class Grade:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        out = f"Name:{self.name}"
        return out

    def print_info(self):
        out = self.get_info()
        print(out)
