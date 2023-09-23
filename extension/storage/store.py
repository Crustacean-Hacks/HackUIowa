from dotenv import load_dotenv, find_dotenv
import os
import certifi
from pymongo import MongoClient
from datetime import date


data_collection = None

def load():
  load_dotenv(find_dotenv())
  password = os.environ.get("MONGODB_PWD")
  connection_string = f"mongodb+srv://i0dev:{password}@logins.qy8thq3.mongodb.net/?retryWrites=true&w=majority"
  client = MongoClient(connection_string, tlsCAFile=certifi.where())

  storage_db = client.storage
  data_collection = storage_db.data


def store(storageID, website):

  # get the number of the month of the year
  month = date.now().strftime("%m")
  day = date.now().strftime("%d")
  year = date.now().strftime("%Y")


  

  data_collection.insert_one()