# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import time

import pymongo
import bson
from pymongo import *
from scrapy.conf import settings

from JDSpider.tool.get_comment import get_comment, get_comment2

""" # 好评率
    goodRateShow = scrapy.Field()
    # 差评
    poorCountStr = scrapy.Field()
    # 中评
    generalCountStr = scrapy.Field()
    # 好评
    goodCountStr = scrapy.Field()"""


class JdspiderPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbName = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=host, port=port)
        tdb = client[dbName]
        self.post = tdb[settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
        data = dict(item)
        doc = {
            'goodCountStr': data['goodCountStr'],
            'generalCountStr': data['generalCountStr'],
            'poorCountStr': data['poorCountStr'],
            'goodRateShow': data['goodRateShow'],
            'product_id': data['product_id'],
            'product_name': data['product_name'],
            'shop': data['shop'],
            'product_color': data['product_color'],
            'version': data['version'],
            'Brand': data['Brand'],
            'price': data['price'],
            # 'json_url': data['json_url'],
               }
        self.post.insert_one(doc)
        # time.sleep(0.5)
        # if data['generalCountStr'] != 0:
        #     get_comment(data['product_id'])
        # elif data['generalCountStr'] == 0:
        #     get_comment2(data['product_id'])
        return item

