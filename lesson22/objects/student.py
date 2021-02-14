class Student:
    def __init__(self, username, age, grade):
        self.username = username
        self.age = age
        self.grade = grade

    def get_info(self):
        output = f"StudentName:{self.username},StudentAge:{self.age}"
        return output

    def print_info(self):
        output = self.get_info() + "," + self.grade.get_info()
        print(output)
