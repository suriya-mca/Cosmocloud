from decouple import config
from pymongo import MongoClient
from bson import ObjectId


client = MongoClient(config('MONGO_URL'))
db = client["student_db"]
collection = db["students"]