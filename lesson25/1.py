#база данных - sqllite3
#sql
#база данных -> таблиц -> данных
import sqlite3
connection = sqlite3.connect("mydatabase.db")
cursor = connection.cursor()
sql = """
create table if not exists users(
    id int,
    username text,
    password text
)
"""
cursor.execute(sql)
#создать данные
# sql_insert = """
# insert into users
# (id, username, password)
# values
# (2,'yerassyl123','1234564434')
# """
# cursorInsert = connection.cursor()
# cursorInsert.execute(sql_insert)
# connection.commit()
selectSql = "select * from users"
cursorSelect = connection.cursor()
cursorSelect.execute(selectSql)
data = cursorSelect.fetchall()
for i in data:
    print(i)
