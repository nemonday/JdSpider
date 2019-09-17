# -*- coding: utf-8 -*-
import json
import re
import time
from copy import deepcopy
import jsonpath
import scrapy
from JDSpider.tool.url_text import *
from JDSpider.items import JdspiderItem
from JDSpider.tool.get_comment import get_comment
from scrapy_redis.spiders import RedisCrawlSpider
from urllib.parse import unquote

class JindongSpider(RedisCrawlSpider):
    name = 'jindong'
    allowed_domains = ['https://www.jd.com/']
    redis_key = 'jindong:start_urls'
    # def start_requests(self):
    #     base_urls = 'https://list.jd.com/list.html?cat=9987,653,655&ev=exbrand_{}&JL=3_{}'
    #
    #     for i in range(10000):
    #         try:
    #             request_url = base_urls.format(base_urls_number[i], base_urls_project[i])
    #             # print(request_url)
    #             yield scrapy.Request(request_url, callback=self.parse)
    #         except:
    #             pass

    def parse(self, response):
        # Brand = re.match(r'(^.*C_)(.*)', response.url).group(2)
        # result = unquote(Brand,'utf-8')
        project_list = response.xpath('//div[@class="p-name"]')
        for project in project_list:
            item = JdspiderItem()
            item['Brand'] = '华为（HUAWEI）'
            title_test = project.xpath('normalize-space(./a/em/text())').extract_first()
            title_test_url = 'https:' + project.xpath('normalize-space(./a/@href)').extract_first()
            item['title'] = title_test
            item['title_url'] = title_test_url
            yield scrapy.Request(item['title_url'],
                                 callback=self.product_list_parse, meta={'item': deepcopy(item)}, dont_filter=True)

        callback_url = response.xpath('//a[@class="pn-next"]/@href').extract_first()
        if callback_url:
            print('下一页')
            yield scrapy.Request('https:/' + callback_url, callback=self.parse)

    def product_list_parse(self, response):
        """ 获取产品列表 """
        item = response.meta['item']

        try:
            result = re.search(r'colorSize: \[.*\]', response.text).group()
            result = re.search(r'\[.*\]', result, re.S).group()
            result = re.findall(r'{.*?}', result, re.S)
            for i in result:
                try:
                    item['version'] = eval(i)['版本']
                    item['product_id'] = eval(i)['skuId']
                    item['product_color'] = eval(i)['颜色']
                    item['product_url'] = 'https://item.jd.com/{}.html'.format(item['product_id'])
                    yield scrapy.Request(item['product_url'], callback=self.product_parse,
                                         meta={'item': deepcopy(item)}, dont_filter=True)
                except:
                    pass
        except:
            yield scrapy.Request(response.url,
                                 callback=self.product_parse, meta={'item': deepcopy(item)}, dont_filter=True)

    def product_parse(self, response):
        """ 获得详细页面里面的信息 """
        item = response.meta['item']

        item['shop'] = response.xpath('//*[@id="crumb-wrap"]/div/div[2]/div[2]/div[1]/div/a/text()').extract_first()

        data = (response.xpath('//title/text()').extract_first()).replace('【行情 报价 价格 评测】-京东', "")
        item['product_name'] = data.replace('【图片 价格 品牌 报价】-京东', "")
        # 获取评论,好评,差评
        # time.sleep(0.1)
        try:
            yield scrapy.Request(deepcopy(json_text.format(item['product_id'], 0)),
                                 callback=self.goods_info, meta={'item': deepcopy(item)}, dont_filter=True)
        except:
            pass

    def goods_info(self, response):
        """ 获取评论,好评,差评"""
        item = response.meta['item']
        try:
            item['goodRateShow'] = json.loads(response.text)['productCommentSummary']['goodRateShow']
            item['poorCountStr'] = json.loads(response.text)['productCommentSummary']['poorCountStr']
            item['generalCountStr'] = json.loads(response.text)['productCommentSummary']['generalCountStr']
            item['goodCountStr'] = json.loads(response.text)['productCommentSummary']['goodCountStr']
            item['json_url'] = response.url

            yield scrapy.Request(json_price.format(item['product_id']),
                                 callback=self.get_price, meta={'item': item}, dont_filter=True)
        except:
            print('德玛西亚')

    def get_price(self, response):
        """ 获取价格 """
        item = response.meta['item']
        price_data = json.loads(response.text)
        item['price'] = jsonpath.jsonpath(price_data, '$..p')[0]
        item['price_url'] = response.url
        yield item