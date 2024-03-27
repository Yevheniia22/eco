from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/more_com/")
def more_com():
    return render_template("more_com.html")


@app.route("/more_posts/")
def more_posts():
    return render_template("more_posts.html")


@app.route("/login/")
def login():
    return render_template("login.html")


@app.route("/signup/")
def signup():
    return render_template("signup.html")


@app.route("/account/")
def account():
    return render_template("account.html")


@app.route("/post/")
def post():
    return render_template("signup.html")
# якщо зайшов на сайт без акаунта, то воно буде спочатку просити зайти або зареєструватися
# якщо акаунт є то буде робитися новий пост і додаватися на сторінку в more


app.run(port=786858, debug=True)
