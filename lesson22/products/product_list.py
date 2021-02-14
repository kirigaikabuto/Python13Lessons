class ProductList:
    def __init__(self, products):
        self.products = products

    def print_info(self):
        for i in self.products:
            print(i.get_info())

    def get_average_price(self):
        sumi = 0
        for i in self.products:
            sumi += i.price
        return sumi // len(self.products)

    def filter_by_average_price(self):
        avg = self.get_average_price()
        for i in self.products:
            if i.price >= avg:
                print(i.get_info())
