from dotenv import load_dotenv, find_dotenv
import os
from os import environ as env
import json
from authlib.integrations.flask_client import OAuth
from flask import Flask, redirect, render_template, session, url_for, request
from flask_cors import CORS
import store as DataStore

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

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

        print("Received:" + json.loads(request.json))

        DataStore.store(apikey, websites, seconds)

        return '{"success": true}'


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    port = os.environ.get("PORT")
    ip = os.environ.get("IP")
    debug = os.environ.get("DEBUG")
    fullchain = os.environ.get("SSL_FULLCHAIN")
    privkey = os.environ.get("SSL_PRIVKEY")
    app.run(debug=debug, port=port, host=ip, ssl_context=(fullchain, privkey))