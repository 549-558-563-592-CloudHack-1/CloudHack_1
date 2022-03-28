from datetime import datetime
from pymongo import MongoClient
user = 'user1'
password = 'user1'
host = 'mongo-express-deployment'
port = '8081'
conn_string = f'mongodb://{user}:{password}@{host}:{port}'

db = MongoClient(conn_string).blog

def insert(title,author,createdAt):
    try:
        db.posts.insert_one({"title": title, "author": author, "createdAt": createdAt})
    except:
        return -1

insert("Shadow City","Taran N. Khan",datetime("2019-10-12"))
insert("In Cold Blood","Truman Capote",datetime("1965-05-16"))
insert("Breakfast at Tiffany's","Truman Capote",datetime("1958-10-28"))
