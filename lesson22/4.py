# from products.product import Product
# from products.category import Category
from products import *

c1 = Category("category1")
c2 = Category("category2")
p1 = Product("product1", 300, c1)
p2 = Product("product2", 400, c2)
print(p1.get_info())
print(p2.get_info())
