# class
class Computer:
    def __init__(self, n, r, process, price):
        self.name = n
        self.ram = r
        self.processor = process
        self.price = price


# object
computer1 = Computer(n="acer predator", r=8, process="intel core i7", price=10000)
computer2 = Computer(n="acer predator123", r=8, process="intel core i7", price=103000)
computers = [computer1, computer2]
sumi = 0
for i in computers:
    sumi += i.price
print(sumi)
