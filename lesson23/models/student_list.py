class StudentList:
    def __init__(self, students):
        self.students = students

    def print_oldest(self):
        maxi = 0
        student = None
        for i in self.students:
            if i.age > maxi:
                maxi = i.age
                student = i
        student.print_info()
