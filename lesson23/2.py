from models import *

grade1 = Grade(name="11b")
student1 = Student(name="student1", age=16, grade=grade1)
student1.print_info()
