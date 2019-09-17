import jieba
import pandas as pd
# data = '真是好久好久没来哈皮娜拉野生动物园了，记忆里还是小时候三四年级学校组织春游去的银河系'
# data2 = '非常好非常好非常好非常好'

# 精确模式
list1 = ['非常','好']
list2 = []

# cut_data1 = jieba.cut(data2)
# test_data = '/'.join(cut_data1)
# print(test_data)

data = pd.read_csv('/home/nemo/PycharmProjects/JDSpider/JDSpider/doc/meidi_jd_neg.txt',
                   encoding='utf-8', header=None)
for i in data[0]:
    print('/'.join(jieba.cut(data)))

