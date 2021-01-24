from utils import saveToJsonFile, getDataFromJsonFile

students = getDataFromJsonFile("./data/students.json")
teachers = getDataFromJsonFile("./data/teachers.json")


def studentStart():
    print("[1]Login")
    print("[2]Back")
    num = input()
    if num == "1":
        pass
    elif num == "2":
        start()
    else:
        print("There is no choice")
        studentStart()


def start():
    print("[1]Teacher")
    print("[2]Student")
    print("[3]Exit")
    num = input()
    if num == "1":
        pass
    elif num == "2":
        studentStart()
    elif num == "3":
        exit()
    else:
        print("There is no choice")
        start()


start()
