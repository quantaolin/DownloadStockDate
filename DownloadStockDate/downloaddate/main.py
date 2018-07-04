'''
Created on 2018-07-05 01:27

@author: linqt
'''
from pymongo import MongoClient

conn = MongoClient('127.0.0.1', 27017)
db = conn.mydb
my_set = db.test_set
my_set.insert({"name":"zhangsan","age":18})
print(my_set.find_one({"name":"zhangsan"}))