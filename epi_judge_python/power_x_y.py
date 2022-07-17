from test_framework import generic_test


def power(x: float, y: int) -> float:
    answer =1.0
    if y<0:
        y = -y
        x = 1/x
    while (y!=0):
        if y%2==1:
            answer *=x
        x*=x
        y >>=1

    return answer


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
