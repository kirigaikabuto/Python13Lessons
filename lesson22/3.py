from objects import *

g1 = Grade("11a")
g2 = Grade("11b")
g3 = Grade("11c")

st1 = Student("student1", 15, g1)
st12 = Student("student2", 16, g1)

st2 = Student("student3", 17, g2)
st21 = Student("student4", 18, g2)

st3 = Student("student5", 19, g3)
st31 = Student("student6", 20, g3)

students = [st1, st12, st2, st21, st3, st31]
sl1 = StudentList(students)
# sl1.filter_by_age(15)
# sl1.filter_by_grade_name("11b")
# sl1.filter_by_grade()
sl1.filter_by_ages()