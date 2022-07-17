import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3

def compute_tower_hanoi(num_rings: int) -> List[List[int]]:
    steps=[]

    pegs=[[] for _ in range(NUM_PEGS)]
    for i in range(num_rings,0,-1):
        pegs[0].append(i)
    compute_tower_hanoi_steps(num_rings,pegs,0,1,2,steps)
    return steps
def compute_tower_hanoi_steps(num_rings,pegs,from_peg,to_peg,use_peg,steps):
    if num_rings>0:
        compute_tower_hanoi_steps(num_rings-1, pegs, from_peg, use_peg, to_peg,steps)
        pegs[to_peg].append(pegs[from_peg].pop())
        steps.append([from_peg,to_peg])
        compute_tower_hanoi_steps(num_rings-1, pegs, use_peg, to_peg, from_peg,steps)




@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))
            ] + [[] for _ in range(1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure('Illegal move from {} to {}'.format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure('Pegs doesn\'t place in the right configuration')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('hanoi.py', 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper))
