from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route("/")
def main_page():
    connection = sqlite3.connect("mydatabase.db")
    selectSql = "select * from products"
    cursorSelect = connection.cursor()
    cursorSelect.execute(selectSql)
    data = cursorSelect.fetchall()
    products = []
    for i in data:
        d = {
            "id": i[0],
            "name": i[1],
            "price": i[2],
        }
        products.append(d)
    return render_template("main/main_page.html",products = products)


@app.route("/contacts")
def contact_page():
    print("contact page")
    return "contact page"


if __name__ == "__main__":
    app.run()
