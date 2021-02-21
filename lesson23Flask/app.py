from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    name = "Yerassyl"
    out = "<p><b>Hello</b> Yerassyl</p>"
    return render_template("home.html")


@app.route("/category")
def category():
    out = "<h1>Categories</h1>"
    return out


@app.route("/contacts")
def contacts_page():
    return "Contacts"


if __name__ == "__main__":
    app.run()
