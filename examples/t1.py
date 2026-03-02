# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：https://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：python-office
@代码日期    ：2025/4/13 23:14 
@本段代码的视频说明     ：
'''
from loguru import logger

from pofinance import t1

rate = t1(112.23565656565, 112.36, 700)
logger.info(rate)
