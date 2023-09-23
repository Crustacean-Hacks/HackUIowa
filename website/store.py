from dotenv import load_dotenv, find_dotenv
import os
import certifi
from pymongo import MongoClient
import datetime
import json
import bson


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


def store(database, storageID, website, amountToAdd):
    data_collection = database

    # get the number of the month of the year
    now = datetime.datetime.now()
    month = now.strftime("%m")
    day = now.strftime("%d")
    year = now.strftime("%Y")
    hour = now.strftime("%H")

    mongoObj = data_collection.find_one({"storageID": storageID})
    wasNone = False
    currentObjJson = None
    if mongoObj == None:
        currentObjJson = new_storage(storageID)
        wasNone = True
    else:
        currentObjJson = json.loads(
            data_collection.find_one({"storageID": storageID}).string()
        )
    if currentObjJson == None:
        currentObjJson = new_storage(storageID)

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
            currentObjJson["websites"][website][year][month][day][hour] + amountToAdd
        )
    
    print("Adding " + str(amountToAdd) + " to " + website + " for " + storageID)
    # replace the current object with the edited one
    if wasNone:
        data_collection.insert_one(currentObjJson)
    else:
        data_collection.replace_one({"storageID": storageID}, (currentObjJson))
