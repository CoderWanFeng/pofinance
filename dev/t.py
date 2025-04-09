# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@读者群     ：http://www.python4office.cn/wechat-group/
@学习网站      ：https://www.python-office.com
@代码日期    ：2023/12/21 22:26 
@本段代码的视频说明     ：
'''

import pofinance as pf

# 计算做T的收益
get_money = pf.t0(buy_price=27.71,  # 买入成本
                  sale_price=30,  # 卖出价格
                  num=7000,  # 单笔数量
                  w_rate=2.5 / 10000,  # 手续费，默认万2.5
                  min_rate=5,  # 单笔最低手续费，默认5元
                  stamp_tax=0.5 / 1000  # 印花税，默认千0.5
                  )
# 输出做T的收益
print(get_money)
