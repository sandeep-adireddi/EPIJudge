from test_framework import generic_test
import functools

def compute_binomial_coefficient(n: int, k: int) -> int:
    x_choose_y = [[0]*(k+1 )for _ in range(n+1)]

    return computeXchooseY(n,k,x_choose_y)

def computeXchooseY(n,k,x_choose_y):
    if k in (0,n):
        return 1
    if x_choose_y[n][k]==0:
        without_y = computeXchooseY(n-1, k, x_choose_y)
        with_y = computeXchooseY(n-1, k-1, x_choose_y)
        x_choose_y[n][k]=with_y+without_y
    return x_choose_y[n][k]
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('binomial_coefficients.py',
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
