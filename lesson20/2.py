class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def show(self):
        s = f"A={self.a},B={self.b},C={self.c}"
        print(s)

    def calculateArea(self):
        print("calculate areal")

    def calculatePerimeter(self):
        print(self.a + self.b + self.c)

    def createInMongoDb(self):
        pass


st1 = int(input("A="))
st2 = int(input("B="))
st3 = int(input("C="))
print("start program")
# object created
tr1 = Triangle(a=st1, b=st2, c=st3)
tr1.show()
tr1.calculateArea()
tr1.calculatePerimeter()
tr1.createInMongoDb()
