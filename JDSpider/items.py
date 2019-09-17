# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    title_url = scrapy.Field()
    version = scrapy.Field()
    product_id = scrapy.Field()
    product_color = scrapy.Field()
    product_url = scrapy.Field()
    product_name = scrapy.Field()
    shop = scrapy.Field()
    # 好评率
    goodRateShow = scrapy.Field()
    # 差评
    poorCountStr = scrapy.Field()
    # 中评
    generalCountStr = scrapy.Field()
    # 好评
    goodCountStr = scrapy.Field()
    comment = scrapy.Field()
    json_url = scrapy.Field()
    price = scrapy.Field()
    price_url = scrapy.Field()
    Brand = scrapy.Field()
    # logo = scrapy.Field()

