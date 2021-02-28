import sqlite3

connection = sqlite3.connect("mydatabase.db")
cursor = connection.cursor()
sql = """
create table if not exists products(
    id int,
    name text,
    price int
)
"""
# id = 1
# name = "product1"
# price = 300
# cursor.execute(sql)
# sql_insert = """
# insert into products
# (id, name, price)
# values
# (?,?,?)
# """
# cursorInsert = connection.cursor()
# cursorInsert.execute(sql_insert, [id, name, price])
# connection.commit()
selectSql = "select * from products"
cursorSelect = connection.cursor()
cursorSelect.execute(selectSql)
data = cursorSelect.fetchall()
for i in data:
    print(i)