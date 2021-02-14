class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        out = f"Name:{self.name};Price:{self.price};Category{self.category.get_info()}"
        return out
