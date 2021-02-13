from objects.grade import Grade
from objects.student import Student

g1 = Grade("11b")
st1 = Student("yerassyl", 23, g1)
# print(g1.get_info())
# print(st1.get_info())
st1.print_info()
