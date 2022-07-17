from typing import List

from test_framework import generic_test

def maximum_revenue(coins: List[int]) -> int:
    maximum_revenue_for_range = [[0]*len(coins)for _ in coins]
    return compute_max_revenue_for_range(coins,0,len(coins)-1,maximum_revenue_for_range)
def compute_max_revenue_for_range(coins,start,end,maximum_revenue_for_range):
    if start>end:
        return 0
    if maximum_revenue_for_range[start][end]==0:
        picking_start = coins[start]+min( compute_max_revenue_for_range(coins,start+1,end-1,maximum_revenue_for_range),
                                            compute_max_revenue_for_range(coins, start+2, end, maximum_revenue_for_range) )
        picking_end = coins[end]+min(compute_max_revenue_for_range(coins, start+1, end-1, maximum_revenue_for_range),
                                        compute_max_revenue_for_range(coins, start, end-2, maximum_revenue_for_range))
        maximum_revenue_for_range[start][end] = max(picking_start,picking_end)
    return maximum_revenue_for_range[start][end]
    if len(coins)==2:
        return max(coins)
    if len(coins)==1:
        return coins[0]
    return max(coins[0]+min(maximum_revenue(coins[1:len(coins)-1]),maximum_revenue(coins[2:])),
                coins[-1]+min(maximum_revenue(coins[1:len(coins)-1]),maximum_revenue(coins[:len(coins)-2])))
            
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('picking_up_coins.py',
                                       'picking_up_coins.tsv',
                                       maximum_revenue))
