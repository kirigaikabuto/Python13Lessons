class StudentList:
    def __init__(self, students):
        self.students = students

    def print_info(self):
        for i in self.students:
            i.print_info()
