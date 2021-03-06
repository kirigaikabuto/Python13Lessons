import pymongo
import random
from sms_sender import send_sms

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["university"]
studentsCollection = db["students"]
teachersCollection = db["teachers"]
subjectsCollection = db["subjects"]
scheduleCollection = db["schedule"]
groupsCollection = db["groups"]


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


def resetPassword():
    print("---RESET PASSWORD---")
    phone = input("phone:")
    filter = {
        "phone": phone,
    }
    users = list(studentsCollection.find(filter))
    if len(users) != 0:
        check = phoneNumberVerification(phone)
        if check:
            user = users[0]
            newPassword = input("new password:")
            user["password"] = newPassword
            update = {
                "$set": user
            }
            studentsCollection.update_one(filter, update)
            studentStart()
        else:
            print("Not correct code")
            resetPassword()
    else:
        print("There is no user with that phone number")
        resetPassword()


def studentLogin():
    print("---STUDENT LOGIN---")
    username = input("username:")
    password = input("password:")
    filter = {
        "username": username,
        "password": password,
    }
    users = list(studentsCollection.find(filter))
    if len(users) != 0:
        student = users[0]
        studentMainMenu(student)
    else:
        print("There is no user by this username and password")
        print("[1]Try login")
        print("[2]Reset Password")
        print("[3]Go back")
        num = input("choice:")
        if num == "1":
            studentLogin()
        elif num == "2":
            resetPassword()
        elif num == "3":
            studentStart()


def schedulePrettyShow(schedule):
    schedule_id = schedule["id"]
    group_id = schedule["group_id"]
    teacher_id = schedule["teacher_id"]
    subject_id = schedule["subject_id"]
    filter_group = {
        "id": group_id,
    }
    group = subjectsCollection.find_one(filter_group)
    filter_teacher = {
        "id": teacher_id,
    }
    teacher = teachersCollection.find_one(filter_teacher)
    filter_subject = {
        "id": subject_id,
    }
    subject = subjectsCollection.find_one(filter_subject)
    output = f"№{schedule_id}, {group['name']} {teacher['first_name']} {teacher['last_name']} {subject['name']} {schedule['time']}"
    print(output)


def scheduleStart(student):
    filter = {
        "group_id": student["group_id"]
    }
    schedules = list(scheduleCollection.find(filter))
    for i in schedules:
        schedulePrettyShow(i)


def studentMainMenu(student):
    print("---MAIN MENU---")
    print("Hello " + student["first_name"] + " " + student["last_name"])
    print("[1]Schedule")
    num = int(input("choice:"))
    if num == 1:
        scheduleStart(student)
        studentMainMenu(student)


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
        "id": random.randint(10, 100000000),
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
    studentStart()


def studentStart():
    print("[1]Login")
    print("[2]Register")
    print("[3]Back")
    num = input()
    if num == "1":
        studentLogin()
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
