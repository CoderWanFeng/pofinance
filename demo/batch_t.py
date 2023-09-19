# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信 ：CoderWanFeng : https://mp.weixin.qq.com/s/B1V6KeXc7IOEB8DgXLWv3g
@个人网站 ：www.python-office.com
@Date    ：2023/4/3 23:05 
@Description     ：
'''
from pofinance import MakeT

# pip install pofinance

t = MakeT()

sale_price_num = [(900, 12), (13000, 11),(800, 10)]
res=t.batch_t(sale_price_num)
print(res)
