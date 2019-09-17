import requests
from lxml import etree

url = 'http://tool.manmanbuy.com/historyLowest.aspx?url=https%3a%2f%2fitem.jd.com%2f30412009531.html'

data = requests.get(url)

eroot = etree.HTML(data.text)
result = eroot.xpath('//*[@id="container"]/canvas[2]')
print(result)