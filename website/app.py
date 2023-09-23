from dotenv import load_dotenv, find_dotenv
import os
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

load_dotenv(find_dotenv())
port = os.environ.get("port")
ip = os.environ.get("ip")
debug = os.environ.get("debug")

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/data_post", methods=["POST"])
def data_post():
    website = request.form["website"]
    username = request.form["username"]
    password = request.form["password"]
    print(website, username, password)

    # Handle saving data


if __name__ == "__main__":
    app.run(debug=debug, port=port, host=ip)
