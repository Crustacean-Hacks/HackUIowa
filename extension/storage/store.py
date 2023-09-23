from dotenv import load_dotenv, find_dotenv
import os
import certifi
from pymongo import MongoClient


def load():
  load_dotenv(find_dotenv())
  password = os.environ.get("MONGODB_PWD")
  connection_string = f"mongodb+srv://i0dev:{password}@logins.qy8thq3.mongodb.net/?retryWrites=true&w=majority"
  client = MongoClient(connection_string, tlsCAFile=certifi.where())

  storage_db = client.logins
  data_collection = storage_db.data


def store(storageID, website):
  return