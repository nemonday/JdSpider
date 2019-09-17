import redis

from tool.url_text import base_urls_number, base_urls_project


class redis_proxy(object):
    def __init__(self, host='127.0.0.1', port='6379'):
        """连接redis数据库"""
        self.db = redis.StrictRedis(host=host, port=port, decode_responses=True, db=2)

    def add_redis(self):
        # base_urls = 'https://list.jd.com/list.html?cat=9987,653,655&ev=exbrand_{}&JL=3_{}'
        base_urls = 'https://list.jd.com/list.html?cat=9987,653,655&ev=exbrand_8557&page=3&sort=sort_rank_asc&trans=1&JL=https://list.jd.com/list.html?cat=9987,653,655&ev=exbrand_8557&page={}&sort=sort_rank_asc&trans=1&JL=品牌_华为（HUAWEI）'
        for i in range(51):
            request_url = base_urls.format(i)
            # print(request_url)
            self.db.lpush('jindong:start_urls', request_url)





cls = redis_proxy()
cls.add_redis()


