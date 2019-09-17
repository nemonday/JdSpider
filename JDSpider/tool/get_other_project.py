import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}


def get_title(url):
    data = requests.get(url, headers)
    eroot = etree.HTML(data.text)
    title = eroot.xpath('normalize-space(//div[@class="p-name"]/a/em/text())')
    title_url = 'https:' + eroot.xpath('normalize-space(//div[@class="p-name"]/a/@href)')

    return title, title_url

