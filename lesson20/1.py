# class
class Computer:
    def __init__(self, n, r, process, price):
        self.name = n
        self.ram = r
        self.processor = process
        self.price = price

    # write something
    def printName(self):
        print("it is computer class")

    def calculateSomething(self):
        output = f"Name:{self.name},Price:{self.price}"
        print(output)

    def showSelf(self):
        print(self)


# object1
computer1 = Computer(n="acer predator", r=8, process="intel core i7", price=10000)
# object1
computer2 = Computer(n="acer predator123", r=8, process="intel core i7", price=103000)
computers = [computer1, computer2]
computer1.calculateSomething()
computer2.calculateSomething()
print(computer1)
#computer1 -> self
computer1.showSelf()
print(computer2)
computer2.showSelf()

# sumi = 0
# for i in computers:
#     sumi += i.price
# print(sumi)
