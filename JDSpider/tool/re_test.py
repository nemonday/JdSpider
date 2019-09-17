data = '不好意思！手机买来送给家里人的，试用了几天才来评价。这么实惠的价格买来这样的款式和和品质一个字:' \
       '值&amp;hellip;&amp;hellip;！在京东买电子产品放心。这是我在京东买的第八台手机了！' \
       '还真没碰到什么质量问题！不错&amp;hellip;&amp;hellip;！京东信得过！' \
       '好评&amp;hellip;&amp;hellip;！'


data2 = "第一次用华为手机，亲身体验了一周才给出如下点评，想买的朋友可以参考一下。1.屏幕尺寸很大，有5.99寸，并没有因为720p的分辨率而显示出强烈的颗粒感。2.手机外放@音质不太好，很一般，真的很一般，听音乐不好听。手机听筒打电话时，变声严重，听着不像本人声音，话筒输出也一样，可能为了节约成本导致的结果，希望以后出的新机能够加以改正。插耳机用华为音效听歌还挺好的。3.骁龙450处理器，目前骁龙400系列最新的一款处理器，是骁龙625的降频版，玩王者荣耀开高画质有卡顿感，中特效流畅运行。刺激战场流畅模式可以流畅运行，但是玩以上两款游戏，热感明显。4.这款处理器其实是支持快充的，然而并没有采用快充，很遗憾。5.虽然有1300万+200万像素双摄，但是拍照效果不佳，颜色泛白，同样的1300万像素蓝绿手机的照片效果好很多。6.安卓8.0系统，运行很流畅，功能很齐全。7.32G版本开机剩23.7GB容量。8.3卡槽，可以放2张电话卡和1张内存卡，功能很实用。手机重量略轻。<div class='uploadimgdiv'><img class='uploadimg' border='0'  src='http://img30.360buyimg.com/shaidan/jfs/t22915/62/1088266685/1175/9dfe00a5/5b514106N56054805.jpg' /></div><div class='uploadimgdiv'><img class='uploadimg' border='0'  src='http://img30.360buyimg.com/shaidan/jfs/t21985/301/2330168772/1194/eae51f77/5b514106Nc3e95bdb.jpg' /></div><div class='uploadimgdiv'><img class='uploadimg' border='0'  src='http://img30.360buyimg.com/shaidan/jfs/t21949/219/2334456395/1220/e0240f88/5b514106N880935ea.jpg' /></div><div class='uploadimgdiv'><img class='uploadimg' border='0'  src='http://img30.360buyimg.com/shaidan/jfs/t24277/59/1148172455/1306/ac8a86c/5b514106Ncd6b2f95.jpg' /></div><div class='uploadimgdiv'><img class='uploadimg' border='0'  src='http://img30.360buyimg.com/shaidan/jfs/t22018/153/2322969256/1163/ee1a5350/5b514106Nbc4cdb21.jpg' /></div><div class='uploadimgdiv'><img class='uploadimg' border='0'  src='http://img30.360buyimg.com/shaidan/jfs/t20914/199/2359725771/1270/883dc6ac/5b514106N22fe21e5.jpg' /></div><div class='uploadimgdiv'><img class='uploadimg' border='0'  src='http://img30.360buyimg.com/shaidan/jfs/t24196/33/1095900126/1213/5b9f58d7/5b514106Nf74f6c3d.jpg' /></div><div class='uploadimgdiv'><img class='uploadimg' border='0'  src='http://img30.360buyimg.com/shaidan/jfs/t23689/65/1128520843/1213/bd166098/5b514106N4256bde6.jpg' /></div><div class='uploadimgdiv'><img class='uploadimg' border='0'  src='http://img30.360buyimg." \
        "com/shaidan/jfs/t23812/115/1099857592/1345/feb41a25/5b514106N4b52dffe.jpg' /\n></div>"

data3 = 'https://list.jd.com/list.html?cat=9987,653,655&ev=exbrand_43644&JL=3_%E5%93%81%E7%89%8C_21KE'

data4 = '%E5%8D%8E%E4%B8%BA%EF%BC%88HUAWEI%EF%BC%89'

data5 = ''
import re
from urllib.parse import unquote
# result = re.match(r'(^.*C_)(.*)', data3).group(2)
# result = re.sub(r'<div .*/div>', '', result)

# result = unquote(data4,'utf-8')
# print(result)
#
# from urllib.parse import urlunparse

from datetime import datetime


import time
from urllib.request import urlopen

def time_clock(func):
    def warpper(*args, **kwargs):
        start = time.clock()
        rec = func()
        end = time.clock()
        times = end-start
        print(times)
        return rec
    return warpper

@time_clock
def foo():
    print([i for i in range(1000)])
foo()
