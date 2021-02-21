class Grade:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        out = f"Name:{self.name}"
        print(out)

    def get_info(self):
        out = f"Name:{self.name}"
        return out
