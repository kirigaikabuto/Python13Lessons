from flask import Flask, render_template, request

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

    return render_template("main/main_page.html", mess=message, name=name, products=products, users=users)


@app.route("/login", methods=["GET", "POST"])
def login_page():
    error = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        znak = request.form.get("znak")
        print(znak)
        if len(username) == 0 or len(password) == 0:
            error = "Please write all data"

    return render_template("main/login_page.html", error=error)


@app.route("/calculator", methods=["GET", "POST"])
def calculate_page():
    pass


if __name__ == "__main__":
    app.run()
