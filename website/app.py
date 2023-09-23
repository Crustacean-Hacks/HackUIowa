from dotenv import load_dotenv, find_dotenv
import os
from flask import Flask, render_template, request
from flask_cors import CORS

load_dotenv(find_dotenv())

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/data_post", methods=["POST"])
def data_post():
    if request.method == "POST":
        data = request.json
        apikey = data["apikey"]
        website = data["website"]
        secondsToAdd = data["seconds"]
        return '{"success": "Added' + str(secondsToAdd) + " seconds to " + website + '"}'

def parse_url(url):
    # parse the url so it only returns the domain name. like google.com 
    return "https://www.google.com"

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    port = os.environ.get("PORT")
    ip = os.environ.get("IP")
    debug = os.environ.get("DEBUG")
    app.run(debug=debug, port=port, host=ip)
