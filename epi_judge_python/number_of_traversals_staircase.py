from test_framework import generic_test


def number_of_ways_to_top(top: int, maximum_step: int) -> int:
    number_of_ways_till_now =[0]*(top+1)
    return compute_number_of_ways_till_now(top,maximum_step,number_of_ways_till_now)
def compute_number_of_ways_till_now(current_stair,maximum_step,number_of_ways_till_now):
    if current_stair in (0,1):
        return 1
    elif current_stair<0:
        return 0
    elif number_of_ways_till_now[current_stair]==0:
        for step in range(1,maximum_step+1):
            number_of_ways_till_now[current_stair]+=compute_number_of_ways_till_now(current_stair-step, maximum_step, number_of_ways_till_now)

    return number_of_ways_till_now[current_stair]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_staircase.py',
                                       'number_of_traversals_staircase.tsv',
                                       number_of_ways_to_top))
