from pymongo import MongoClient
from decouple import config


client = MongoClient(config('MONGO_URL'))
db = client["student_db"]
collection = db["students"]