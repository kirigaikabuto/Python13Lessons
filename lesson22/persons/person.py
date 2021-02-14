from database import Mongo


class Person(Mongo):
    def __init__(self, username, age):
        super().__init__("university", "persons")
        self.username = username
        self.age = age

    def save(self):
        d = {
            "username": self.username,
            "age": self.age
        }
        self.create(d)
