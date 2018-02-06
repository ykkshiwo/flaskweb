from flask import Flask, render_template
from flask import request
app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello World! I am yangkangkai</h1>"


@app.route("/user/<name>")
def user(name):
    return render_template('user.html', name=name)


@app.route("/ua")
def index_ua():
    user_agent = request.headers.get("User-Agent")
    return "<p>Your browser is %s</p>" % user_agent


if __name__ == "__main__":
    app.run(debug=True)