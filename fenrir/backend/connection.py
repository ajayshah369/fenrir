from pymongo import MongoClient
from os import environ

MONGO_HOST = environ.get("MONGO_HOST", "localhost")

client = MongoClient(f"mongodb://{MONGO_HOST}:27017/")
db = client["fenrir"]

collections = db["users"]
