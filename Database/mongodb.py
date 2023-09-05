import pymongo
from pymongo import MongoClient


cluster = MongoClient("mongodb+srv://dbUser:Vr6.pNXn_NugLvB@cluster0.su5uviy.mongodb.net/?retryWrites=true&w=majority")

db = cluster["Dino"]
collection = db["5040"]

post = {"_id ":0, "name": "John", "Scor":66}
collection.insert_one(post)



