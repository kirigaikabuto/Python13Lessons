import pymongo
import random
from sms_sender import send_sms

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["university"]
studentsCollection = db["students"]


def phoneNumberVerification(phoneNumber):
    print("---We send code to your phoneNumber---")
    codeCollection = db["codes"]
    code = str(random.randint(10000, 99999))
    d = {
        "code": code
    }
    codeCollection.insert_one(d)
    send_sms(phoneNumber, code)
    codes = codeCollection.find({"code": code})
    inputCode = input('code:')
    for i in codes:
        if inputCode == i["code"]:
            codeCollection.remove(d)
            return True
    codeCollection.remove(d)
    return False


def studentMainMenu():
    print("---MAIN MENU---")


def studentRegister():
    print("---STUDENT REGISTER---")
    phoneNumber = input("phone_number:")
    verified = phoneNumberVerification(phoneNumber)
    if not verified:
        print("Your phoneNumber not verified, repeat registration")
        studentRegister()
    userName = input("username:")
    password = input("password:")
    firstName = input("first_name:")
    lastName = input("last_name:")
    email = input("email:")
    groupId = int(input("group_id:"))
    student = {
        "id": 3,
        "first_name": firstName,
        "last_name": lastName,
        "email": email,
        "phone": phoneNumber,
        "username": userName,
        "password": password,
        "group_id": groupId,
    }
    studentsCollection.insert_one(student)
    print("---Registration ended successfully---")
    studentMainMenu()


def studentStart():
    print("[1]Login")
    print("[2]Register")
    print("[3]Back")
    num = input()
    if num == "1":
        pass
    if num == "2":
        studentRegister()
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
