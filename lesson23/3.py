from models import *

grade1 = Grade(name="11b")
student1 = Student(name="student1", age=16, grade=grade1)
student2 = Student(name="student2", age=20, grade=grade1)
student3 = Student(name="student3", age=10, grade=grade1)
sts = [student1, student2, student3]
studentList = StudentList(students=sts)
studentList.print_oldest()
