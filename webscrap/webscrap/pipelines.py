# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo
class WebscrapPipeline:
    def __init__(self):
        self.conn=pymongo.MongoClient('mongodb+srv://root:root@development.msm0r.mongodb.net/bansh?retryWrites=true&w=majority')
        db=self.conn['bansh']
        self.collection=db['flipcart']
        
        
        
        
    def process_item(self, item, spider):
        # self.collection.insert(dict(item))
        return item
