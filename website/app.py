from dotenv import load_dotenv, find_dotenv
import os
from os import environ as env
import json
from authlib.integrations.flask_client import OAuth
from pymongo.server_api import ServerApi
from flask import Flask, redirect, render_template, session, url_for, request, jsonify
from flask_cors import CORS
import certifi
import uuid
from site_analysis import categorize_website
import pytz
from pymongo import MongoClient
import datetime
from urllib.parse import urlparse, quote_plus, urlencode
import generate_data as GenerateData

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)


tz = pytz.timezone("US/Central")

MONGO_PW = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://i0dev:{MONGO_PW}@logins.qy8thq3.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(
    connection_string, server_api=ServerApi("1"), tlsCAFile=certifi.where()
)

storage_db = client["storage"]
DB_COLL = storage_db["data"]

app = Flask(__name__)

app.secret_key = env.get("APP_SECRET_KEY")
CORS(app)

oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration',
)


@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )


@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("/")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://"
        + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("home", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )


@app.route("/")
def home():
    return render_template(
        "home.html",
        session=session.get("user"),
        pretty=json.dumps(session.get("user"), indent=4),
    )


@app.route("/data_post", methods=["POST"])
def data_post():
    if request.method == "POST":
        data = request.json
        apikey = data["apikey"]
        websites = data["websites"]
        seconds = data["seconds"]

        print("API Key: " + apikey)

        store(apikey, websites, seconds)

        return '{"success": true}'


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/update_dashboard", methods=["POST"])
def update_dashboard():
    data = request.get_json()
    date = data.get("date")  # Get the date parameter from the JSON request
    option = data.get("option")  # Get the option parameter from the JSON request

    if date is None or option is None:
        return jsonify({"error": "Invalid request data"}), 400

    # Depending on the 'option' (e.g., "daily" or "monthly"), retrieve the updated data
    # and format it as needed for your charts

    # For example, you can call functions to generate updated data based on the date and option
    # Replace these with your actual data generation functions
    updated_bar_data = generate_updated_bar_data(date, option)
    updated_pie_data = generate_updated_pie_data(date, option)

    # You can format the data as a dictionary or JSON as per your application's requirements
    response_data = {
        "barData": updated_bar_data,
        "pieData": updated_pie_data
    }

    return jsonify(response_data), 200

# Replace these with your actual data generation functions based on date and option
def generate_updated_bar_data(date, option):
    # Implement your data generation logic here
    # Return the updated bar chart data
    if(option=="daily"):
        return GenerateData.day_data_bar(get_data(getapikey()), date[0:4], date[5:7], date[8:10])
    elif(option=="monthly"):
        return GenerateData.month_data_bar(get_data(getapikey()), date[0:4], date[5:7])
    elif(option=="total"):
        return GenerateData.total_data_bar(get_data(getapikey()))
    else:
        return None
    
    return updated_bar_data

def generate_updated_pie_data(date, option):
    # Implement your data generation logic here
    # Return the updated bar chart data
    if(option=="daily"):
        return GenerateData.day_data_pie(get_data(getapikey()), date[0:4], date[5:7], date[8:10])
    elif(option=="monthly"):
        return GenerateData.month_data_pie(get_data(getapikey()), date[0:4], date[5:7])
    elif(option=="total"):
        return GenerateData.total_data_pie(get_data(getapikey()))
    else:
        return None
    
    return updated_bar_data

@app.route("/dashboard")
def dashboard(year=None, month=None, day=None, total=False):
    if(getapikey() == None):
        return redirect("/account")
    else:
        apikey = getapikey()
        data = get_data(apikey)
        
        currentOption = None
        
        if(year == None):
            if(total): # show all-time data
                bargraph = GenerateData.total_data_bar(data)
                piegraph = GenerateData.total_data_pie(data)
                currentOption = "total"
            else: # Default to today's stats
                now = datetime.datetime.now(tz)
                
                month = now.strftime("%m")
                day = now.strftime("%d")
                year = now.strftime("%Y")

                print('year', year)
                print('month', month)
                print('day', day)
                
                bargraph = GenerateData.day_data_bar(data, year, month, day)
                piegraph = GenerateData.day_data_pie(data, year, month, day)
                currentOption = "daily"
        else:
            if(day == None): # Month data
                bargraph = GenerateData.month_data_bar(data, year, month)
                piegraph = GenerateData.month_data_pie(data, year, month)
                currentOption = "month"
            else: # Day data
                bargraph = GenerateData.day_data_bar(data, year, month, day)
                piegraph = GenerateData.day_data_pie(data, year, month, day)
                currentOption = "daily"
                
        return render_template(
            "dashboard.html", examplebargraph=bargraph, examplepiegraph=piegraph,
            year=year, month=month, day=day, total=total, currentOption=currentOption
    )

def get_data(apikey):
    return DB_COLL.find_one({"storageID": apikey})


def getapikey():
    if session.get("user") == None:
        return None
    else:
        coll = storage_db["users"]
        output = coll.find_one(
            {"email": session.get("user").get("userinfo").get("email")}
        )
        if output == None:
            apikey = uuid.uuid4().__str__()
            coll.insert_one(
                {
                    "email": session.get("user").get("userinfo").get("email"),
                    "apikey": apikey,
                }
            )
            return apikey
        else:
            return output.get("apikey")


@app.route("/account")
def account():
    return render_template(
        "account.html", session=session.get("user"), apikey=getapikey()
    )


def get_category(clean_url):
    response = storage_db["category"].find_one({"url": clean_url})
    if response == None:
        category = categorize_website(clean_url)
        category = category.lower()
        storage_db["category"].insert_one({"url": clean_url, "category": category})
        return category
    else:
        return response.get("category")


def store(storageID, websites, amountToAdd):
    wasNone = False
    mongoObj = DB_COLL.find_one({"storageID": storageID})
    now = datetime.datetime.now(tz)
    month = now.strftime("%m")
    day = now.strftime("%d")
    year = now.strftime("%Y")
    hour = now.strftime("%H")
    currentObjJson = None
    if mongoObj == None:
        currentObjJson = new_storage(storageID)
        wasNone = True
    else:
        currentObjJson = mongoObj

    for website in websites:
        website = parse_url(website)
        if currentObjJson["websites"].get(website) == None:
            currentObjJson["websites"][website] = {}

        if currentObjJson["websites"][website].get(year) == None:
            currentObjJson["websites"][website][year] = {}

        if currentObjJson["websites"][website][year].get(month) == None:
            currentObjJson["websites"][website][year][month] = {}

        if currentObjJson["websites"][website][year][month].get(day) == None:
            currentObjJson["websites"][website][year][month][day] = {}

        if currentObjJson["websites"][website][year][month][day].get(hour) == None:
            currentObjJson["websites"][website][year][month][day][hour] = amountToAdd
        else:
            currentObjJson["websites"][website][year][month][day][hour] = (
                currentObjJson["websites"][website][year][month][day][hour]
                + amountToAdd
            )

    # replace the current object with the edited one
    if wasNone:
        DB_COLL.insert_one(currentObjJson)
    else:
        DB_COLL.replace_one({"storageID": storageID}, currentObjJson)


def new_storage(storageID):
    new_json = {"storageID": storageID, "websites": {}}
    return new_json


# parse the url so it only returns the domain name. like "google.com" or "netflix.com"
def parse_url(url):
    # Parse the URL
    parsed_url = urlparse(url)

    # Extract the domain (hostname), includes www. and other subdomains
    hostname = parsed_url.hostname

    return hostname


if __name__ == "__main__":
    port = os.environ.get("PORT")
    ip = os.environ.get("IP")
    debug = os.environ.get("DEBUG")
    fullchain = os.environ.get("SSL_FULLCHAIN")
    privkey = os.environ.get("SSL_PRIVKEY")
    if ip != "localhost":
        app.run(debug=debug, port=port, host=ip, ssl_context=(fullchain, privkey))
    else:
        app.run(debug=debug, port=port, host=ip)
