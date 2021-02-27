from flask import Flask, render_template

products = [
    "product1",
    "product2",
    "product3"
]

app = Flask(__name__)


@app.route("/")
def main_page():
    message = "Hello my name is Yerassyl"
    name = "yerassyl"
    return render_template("main/main_page.html", mess=message, name=name)


if __name__ == "__main__":
    app.run()
