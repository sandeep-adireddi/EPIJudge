from typing import List

from test_framework import generic_test

def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_till_now = prices[0]
    profit = 0.0
    for i in range(1,len(prices)):
        profit = max(profit,prices[i]-min_till_now)
        min_till_now = min(min_till_now,prices[i])
    return profit
def buy_and_sell_stock_twice(prices: List[float]) -> float:
    forward_pass = []
    min_till_now = prices[0]
    max_profit = 0
    for i in range(1,len(prices)):
        min_till_now = min(min_till_now,prices[i])
        max_profit = max(max_profit, prices[i]-min_till_now)
        forward_pass.append(max_profit)
        
    backward_pass = []
    max_till_now = prices[-1]

    max_profit = 0
    for i in range(len(prices)-1,0,-1):
       
        max_till_now = max(max_till_now,prices[i])
        max_profit =  max(max_profit,max_till_now-prices[i]+forward_pass[i-1])
       


    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
