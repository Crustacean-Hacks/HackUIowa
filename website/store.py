from dotenv import load_dotenv, find_dotenv
import os
import certifi
from pymongo import MongoClient
import datetime
from urllib.parse import urlparse


def load():
    load_dotenv(find_dotenv())
    password = os.environ.get("MONGODB_PWD")

    connection_string = f"mongodb+srv://i0dev:{password}@logins.qy8thq3.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(connection_string, tlsCAFile=certifi.where())

    storage_db = client.storage
    return storage_db.data


def new_storage(storageID):
    new_json = {"storageID": storageID, "websites": {}}
    return new_json


# parse the url so it only returns the domain name. like "google.com" or "netflix.com"
def parse_url(url):
    # Parse the URL
    parsed_url = urlparse(url)

    # Extract the domain (hostname), includes www. and other subdomains
    hostname = parsed_url.hostname

    return hostname.split(".")[-2] + "." + hostname.split(".")[-1]


def store(storageID, websites, amountToAdd):
    data_collection = load()
    wasNone = False
    mongoObj = data_collection.find_one({"storageID": storageID})
    now = datetime.datetime.now()
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

    print("Current object: " + str(currentObjJson))

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

    print("Final object: " + str(currentObjJson))

    # replace the current object with the edited one
    if wasNone:
        data_collection.insert_one(currentObjJson)
    else:
        data_collection.replace_one({"storageID": storageID}, currentObjJson)


store(
    "test",
    ["https://www.google.com", "https://www.netflix.com"],
    1,
)
