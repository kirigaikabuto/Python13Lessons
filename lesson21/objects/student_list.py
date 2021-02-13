class StudentList:
    def __init__(self, students):
        self.students = students

    def print_info(self):
        for i in self.students:
            i.print_info()

    def filter_by_age(self, age):
        for i in self.students:
            if i.age >= age:
                i.print_info()
