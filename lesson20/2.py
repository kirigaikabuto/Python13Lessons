class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        print("object is created")

    def show(self):
        s = f"A={self.a},B={self.b},C={self.c}"
        print(s)


st1 = int(input("A="))
st2 = int(input("B="))
st3 = int(input("C="))
print("start program")
# object created
tr1 = Triangle(a=st1, b=st2, c=st3)
