# -*- coding: UTF-8 -*-
'''
@Author  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/6/2 22:52
@Description     ：
'''

from decimal import Decimal

RATE_LINE = 10000 * 2


def t0(buy_price: float, sale_price: float, num: int, w_rate: float = 2.5 / 10000, min_rate: int = 5,
       stamp_tax=1 / 1000, ) -> float:
    """
    计算做T的收益
    Args:
        buy_price: 买入成本
        sale_price: 卖出价格
        num: 单笔数量
        w_rate: 手续费，默认万2.5
        min_rate: 单笔最低手续费，默认5元
        stamp_tax: 印花税，默认千1

    Returns: 做T后的收益金额

    """
    buy_money = Decimal(str(buy_price)) * num  # 买入的价格
    base_rate = min_rate if buy_money <= RATE_LINE else buy_money * w_rate

    sale_money = Decimal(str(sale_price)) * num
    sale_rate = min_rate if sale_money <= RATE_LINE else sale_money * w_rate

    sale_tax = sale_money * Decimal(str(stamp_tax))  # 印花税
    stock_returns = sale_money - buy_money - base_rate - sale_rate - sale_tax
    return stock_returns


if __name__ == '__main__':
    print(t0(11.99, 12.26, 700))
