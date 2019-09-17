import json
import re

import pymongo
import time
# from JDSpider.settings import *
import jsonpath

from JDSpider.settings import COMMENT_PAGE
import requests
from JDSpider.tool.url_text import *
from bson.objectid import ObjectId
MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'JD_PHONE'
MONGODB_DOCNAME = 'phone'

COMMENT_PAGE = 30

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

host = MONGODB_HOST
port = MONGODB_PORT
dbName = MONGODB_DBNAME
client = pymongo.MongoClient(host=host, port=port)
tdb = client[dbName]
post = tdb[MONGODB_DOCNAME]


def get_comment(product_id):
    for page in range(COMMENT_PAGE):
        url = json_text.format(product_id, page)
        data = requests.get(url, headers)
        try:
            comment_data = json.loads(data.text)['comments']
            data_list = jsonpath.jsonpath(comment_data, '$..content')
            for data in data_list[2:]:
                result = re.sub(r'&amp;|hellip;|&|\n|此用户未填写评价内容|[.\n]', '', data)
                result = re.sub(r'<div .*/div>', '', result)
                post.update(
                    {"product_id": product_id},
                    {"$addToSet": {"comment": result}},
                    upsert=True
                                )

        except:
            pass


def get_comment2(product_id):
    for page in range(1):
        url = json_text.format(product_id, page)
        data = requests.get(url, headers)
        try:
            comment_data = json.loads(data.text)['comments']
            data_list = jsonpath.jsonpath(comment_data, '$..content')
            for data in data_list[2:]:
                result = re.sub(r'&amp;|hellip;|&|\n|此用户未填写评价内容|[.\n]', '', data)
                result = re.sub(r'<div .*/div>', '', result)
                post.update(
                    {"product_id": product_id},
                    {"$addToSet": {"comment": result}},
                    upsert=True
                                )

        except:
            pass
#


# get_comment(3133811)