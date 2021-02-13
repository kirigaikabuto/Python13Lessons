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

    def filter_by_grade_name(self, name):
        pass

    def get_students_name_by_grade_name(self, name):
        students = []
        for i in self.students:
            if i.grade.name == name:
                students.append(i.username)
        return students

    def filter_by_grade(self):
        grades_names = ["11a", "11b", "11c"]
        d = {}
        for i in grades_names:
            # code
            d[i] = self.get_students_name_by_grade_name(i)
        print(d)
