groups = [
    {
        "id": 1,
        "name": "it1601",
    },
    {
        "id": 2,
        "name": "it1701",
    }
]

students = [
    {
        "id": 1,
        "first_name": "yerassyl",
        "last_name": "tleugazy",
        "email": "tleugazy98@gmail.com",
        "phone": "87086394516",
        "username": "kirigaikabuto",
        "password": "passanya99",
        "group_id": 2,
    },
    {
        "id": 2,
        "first_name": "anel",
        "last_name": "tleugazy",
        "email": "anel98@gmail.com",
        "phone": "87086394516",
        "username": "kawaianel",
        "password": "passanya99",
        "group_id": 1,
    },
    {
        "id": 3,
        "first_name": "student3",
        "last_name": "student3",
        "email": "student3@gmail.com",
        "phone": "+77086394516",
        "username": "student3",
        "password": "student3",
        "group_id": 1,
    },
]

teachers = [
    {
        "id": 1,
        "first_name": "teacher1",
        "last_name": "teacher1",
        "email": "teacher1@gmail.com",
        "phone": "87086394516",
        "username": "teacher1",
        "password": "teacher1",
    },
    {
        "id": 2,
        "first_name": "anel",
        "last_name": "tleugazy",
        "email": "teacher2@gmail.com",
        "phone": "87086394516",
        "username": "teacher2",
        "password": "teacher2",
    },
]

subjects = [
    {
        "id": 1,
        "name": "math",
        "credit": 3,
    },
    {
        "id": 2,
        "name": "algebra",
        "credit": 4,
    }
]

schedule = [
    {
        "id": 1,
        "group_id": 2,
        "subject_id": 1,
        "teacher_id": 2,
        "time": "24.01.2021",
    },
    {
        "id": 1,
        "group_id": 1,
        "subject_id": 2,
        "teacher_id": 1,
        "time": "25.01.2021",
    },
]

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["university"]
# groupsCollection = db["groups"]
# groupsCollection.insert_many(groups)
# studentsCollection = db["students"]
# studentsCollection.insert_many(students)
# teachersCollection = db["teachers"]
# teachersCollection.insert_many(teachers)
db["students"].insert_one(students[2])
