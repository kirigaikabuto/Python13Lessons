from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    name = "Yerassyl"
    return name


@app.route("/category")
def category():
    return "Categories"


@app.route("/contacts")
def contacts_page():
    return "Contacts"


if __name__ == "__main__":
    app.run()
