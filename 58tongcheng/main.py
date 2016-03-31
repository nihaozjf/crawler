#-*-coding:utf-8 -*-
import multiprocessing as mul
from multiprocessing import process
import pymongo
client = pymongo.MongoClient('localhost',27017)
db = client['crawler']
item_url_db= db['item_url']
item_info_db = db['item_info']
item_urls=[item['item_url'] for item in item_url_db.find()]
item_info_urls=[item['item_url'] for item in item_info_db.find()]
print item_url_db.find().count()
print item_info_db.find().count()



