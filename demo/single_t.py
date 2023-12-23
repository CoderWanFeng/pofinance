# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信 ：CoderWanFeng : https://mp.weixin.qq.com/s/Nt8E8vC-ZsoN1McTOYbY2g
@个人网站 ：www.python-office.com
@Date    ：2023/4/3 23:05 
@Description     ：
'''
from pofinance import MakeT
import pofinance as pf
# pip install pofinance

t = MakeT()
print(t.single_t(27.11, 26.9, 300))

print(pf.t0(12.2, 12.3, 1000))
