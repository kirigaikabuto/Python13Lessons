from flask import Flask, render_template

products = [
    "product1",
    "product2",
    "product3"
]

users = [
    {
        "username": "user1",
        "salary": 100,
    },
    {
        "username": "user2",
        "salary": 200,
    },
    {
        "username": "user3",
        "salary": 300,
    }
]
app = Flask(__name__)


@app.route("/")
def main_page():
    message = "Hello my name is Yerassyl"
    name = "yerassyl"

    return render_template("main/main_page.html", mess=message, name=name, products=products)


if __name__ == "__main__":
    app.run()
