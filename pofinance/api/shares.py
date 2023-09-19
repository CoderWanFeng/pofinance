# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信 ：CoderWanFeng : https://mp.weixin.qq.com/s/B1V6KeXc7IOEB8DgXLWv3g
@个人网站 ：www.python-office.com
@Date    ：2023/6/2 22:52
@Description     ：
'''

from decimal import Decimal


def t0(buy_price: float, sale_price: float, num: int, w_rate: float = 2.5 / 10000, min_rate: int = 5,
       stamp_tax=0.5 / 1000) -> float:
    """
    计算做T的收益
    Args:
        buy_price: 买入成本
        sale_price: 卖出价格
        num: 单笔数量
        w_rate: 手续费，默认万2.5
        min_rate: 单笔最低手续费，默认5元
        stamp_tax: 印花税，默认千0.5

    Returns: 做T后的收益金额

    """
    w_rate = Decimal(str(w_rate))
    buy_money = Decimal(str(buy_price)) * num  # 买入的价格
    base_rate = min_rate if buy_money * w_rate <= min_rate else buy_money * w_rate

    sale_money = Decimal(str(sale_price)) * num
    sale_rate = min_rate if sale_money * w_rate <= min_rate else sale_money * w_rate

    sale_tax = sale_money * Decimal(str(stamp_tax))  # 印花税
    stock_returns = sale_money - buy_money - base_rate - sale_rate - sale_tax
    return stock_returns


class MakeT():
    def __init__(self, w_rate: float = 2.5 / 10000, min_rate: int = 5, stamp_tax=0.5 / 1000, RATE_LINE=10000 * 2):
        """
        加载手续费
        Args:
            w_rate: 手续费，默认万2.5
            min_rate: 单笔最低手续费，默认5元
            stamp_tax: 印花税，默认千0.5
        """
        self.w_rate = Decimal(str(w_rate))
        self.min_rate = Decimal(str(min_rate))
        self.stamp_tax = Decimal(str(stamp_tax))

    def cal_buy_cost(self, buy_price, num):
        """
        计算买入的成本
        Args:
            sale_price: 买入价格
            num: 买入数量

        Returns:
            买入价格，买入成本
        """
        buy_money = Decimal(str(buy_price)) * num  # 买入的价格
        buy_rate = self.min_rate if buy_money * self.w_rate <= self.min_rate else buy_money * self.w_rate
        return buy_money, buy_rate

    def cal_sale_cost(self, sale_price, num):
        """
        计算卖出的成本
        Args:
            sale_price: 卖出价格
            num: 卖出数量

        Returns:
            卖出价格，卖出成本
        """
        sale_money = Decimal(str(sale_price)) * num
        sale_rate = self.min_rate if sale_money * self.w_rate <= self.min_rate else sale_money * self.w_rate
        sale_tax = sale_money * self.stamp_tax  # 印花税
        return sale_money, sale_rate + sale_tax

    def single_t(self, buy_price: float, sale_price: float, num: int) -> float:
        """
        计算做T的收益
        Args:
            buy_price: 买入成本
            sale_price: 卖出价格
            num: 单笔数量
        Returns: 做T后的收益金额
        """
        buy_money, buy_rate = self.cal_buy_cost(buy_price, num)
        sale_money, sale_rate = self.cal_sale_cost(sale_price, num)
        stock_returns = sale_money - buy_money - buy_rate - sale_rate
        return stock_returns

    def batch_t(self, sale_price_num: list):
        """
        批量卖出，一次买入，求最低收益价格
        Args:
            sale_price_num: 批量卖出的数据，格式： [(500, 27.33), (300, 24.67), (数量, 价格)]

        Returns:
            批量卖出的全部数量，一次全部买入的最低盈利价格
        """
        base_price = 0
        sum_num = 0  # 总股数
        compare_goog_list = []
        while base_price < max([item[1] for item in sale_price_num]):
            sum_num = 0  # 股票总数
            sale_good_list = []  # 每次交易的收益
            for item in sale_price_num:
                sale_num = item[0]
                sum_num += sale_num
                sale_price = item[1]
                sale_good_list.append(self.single_t(base_price, sale_price, sale_num))
            if sum(sale_good_list) > 0 and sum(sale_good_list) - self.cal_buy_cost(base_price, sum_num)[1] > 0:
                compare_goog_list.append((base_price, sum(sale_good_list) - self.cal_buy_cost(base_price, sum_num)[1]))
            base_price = base_price + 0.01
        return f"一次性买出的总股数：{sum_num}，最高价格为：{min(compare_goog_list, key=lambda t: t[1])[0]}，最小收益为： {min(compare_goog_list, key=lambda t: t[1])[1]}"


if __name__ == '__main__':
    s_p = [(500, 27.33), (300, 26.9)]

    # print(t1(s_p))

    # print(t0(27.11, 26.9, 300))
    # print(t0(27.11, 27.33, 500))

    # t = MakeT()
    # print(t.single_t(27.11, 26.9, 300))
    # print(t.batch_t(s_p))
    a = [('a', 2), ('ee', 3), ('mm', 4), ('x', 1)]
    a = [(0, 22042), (0.01, 22022), (0.02, 3), ]
    print(min(a, key=lambda t: t[1]))
