from datetime import datetime
from pymongo import MongoClient
user = 'user1'
password = 'user1'
host = 'mongodb-service'
port = '27017'
conn_string = f'mongodb://{user}:{password}@{host}:{port}'

db = MongoClient(conn_string).blog
def insert(title,author,createdAt):
    try:
        db.posts.insert_one({"title": title, "author": author, "createdAt": createdAt})
    except:
        return -1

insert("Shadow City","Taran N. Khan",datetime.strptime("2019-10-12","%Y-%m-%d"))
insert("In Cold Blood","Truman Capote",datetime.strptime("1965-05-16","%Y-%m-%d"))
insert("Breakfast at Tiffany's","Truman Capote",datetime.strptime("1958-10-28","%Y-%m-%d"))