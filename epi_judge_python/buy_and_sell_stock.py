from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_till_now = prices[0]
    profit = 0.0
    for i in range(1,len(prices)):
        profit = max(profit,prices[i]-min_till_now)
        min_till_now = min(min_till_now,prices[i])
    return profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
