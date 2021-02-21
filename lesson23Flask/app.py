from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    name = "Yerassyl"
    out = "<p><b>Hello</b> Yerassyl</p>"
    return out


@app.route("/category")
def category():
    out = "<h1>Categories</h1>"
    return out


@app.route("/contacts")
def contacts_page():
    return "Contacts"


if __name__ == "__main__":
    app.run()
