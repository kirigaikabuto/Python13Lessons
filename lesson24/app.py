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
    return render_template("main/main_page.html", mess=message)


if __name__ == "__main__":
    app.run()
