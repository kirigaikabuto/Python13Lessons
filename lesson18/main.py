import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["university"]
studentsCollection = db["students"]


def studentStart():
    print("[1]Login")
    print("[3]Register")
    print("[3]Back")
    num = input()
    if num == "1":
        pass
    elif num == "3":
        start()
    else:
        print("There is no choice")
        studentStart()


def teacherStart():
    print("[1]Login")
    print("[2]Register")
    print("[3]Back")
    num = input()
    if num == "1":
        pass
    elif num == "2":
        pass
    elif num == "3":
        start()
    else:
        print("There is no choice")
        teacherStart()


def start():
    print("[1]Teacher")
    print("[2]Student")
    print("[3]Exit")
    num = input()
    if num == "1":
        teacherStart()
    elif num == "2":
        studentStart()
    elif num == "3":
        exit()
    else:
        print("There is no choice")
        start()


start()
