# from products.product import Product
# from products.category import Category
from products import *

c1 = Category("category1")
c2 = Category("category2")
p1 = Product("product1", 300, c1)
p2 = Product("product2", 400, c2)
p3 = Product("product3", 500, c1)
p4 = Product("product4", 600, c2)
products = [p1, p2, p3, p4]
products_list = ProductList(products)
# products_list.print_info()
# print(products_list.get_average_price())
products_list.filter_by_average_price()
