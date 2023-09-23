from dotenv import load_dotenv, find_dotenv
import os
from flask import Flask, render_template, request

load_dotenv(find_dotenv())

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/data_post", methods=["POST"])
def data_post():
    if request.method == "POST":
        # pull the following data from body:
        website = request.form["website"]
        username = request.form["username"]
        password = request.form["password"]
        print(website, username, password)
        return '{"success": true}'


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    port = os.environ.get("PORT")
    ip = os.environ.get("IP")
    debug = os.environ.get("DEBUG")
    app.run(debug=debug, port=port, host=ip)
