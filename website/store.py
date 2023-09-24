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




if __name__ == "__main__":
    store(
        "test",
        ["https://www.google.com", "https://www.netflix.com"],
        1,
    )
