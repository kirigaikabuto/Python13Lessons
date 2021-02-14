from database import Mongo

db = Mongo("university", "test_mongo")
document1 = {
    "name": "document1"
}
document2 = {
    "name": "document2"
}
document3 = {
    "name": "document3"
}
db.create(document1)
db.create(document2)
db.create(document3)
print(db.list())
