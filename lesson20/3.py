class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculateAverageMark(self):
        avg = 0
        sumi = 0
        for i in self.marks:
            sumi += i
        avg = sumi / len(self.marks)
        return avg
        # s = f"Average Mark:{avg}"
        # print(s)

    def show(self):
        avg = self.calculateAverageMark()
        output = f"Name:{self.name},Average Marks:{avg}"
        print(output)


st1 = Student("yerassyl", [1, 2, 3, 4, 5])
st1.show()
