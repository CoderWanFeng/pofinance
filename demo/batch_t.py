# -*- coding: UTF-8 -*-
'''
@Author  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/4/3 23:05 
@Description     ：
'''
from pofinance import MakeT

# pip install pofinance

t = MakeT()
print(t.single_t(27.11, 26.9, 300))
