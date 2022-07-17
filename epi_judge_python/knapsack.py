import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    cache = [[0]*(capacity+1) for _ in range(len(items)+1)]
    for item_index,item in enumerate(items):
        for weight in range(1,capacity+1):
            without_item = cache[item_index][weight]
            with_item = 0 if weight-item.weight<0 else cache[item_index][weight-item.weight]+item.value
            cache[item_index+1][weight] = without_item if item.weight>weight else max(without_item,with_item)




    return cache[-1][-1]


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
