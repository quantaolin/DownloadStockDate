'''
Created on 2018-07-05 01:27

@author: linqt
'''
from pymongo import MongoClient
import tushare as ts

# conn = MongoClient('127.0.0.1', 27017)
# db = conn.mydb
# my_set = db.test_set
# my_set.insert({"name":"zhangsan","age":18})
# print(my_set.find_one({"name":"zhangsan"}))
df = ts.get_h_data('002337',start='2018-07-01',end='2018-07-05')
for indx,item in df.iterrows():
    print(indx)
    print(item['close'])