from test_framework import generic_test


def fibonacci(n: int) -> int:
    dp =[-1]*(n+1)
    return fib_helper(n,dp)
def fib_helper(n,dp):
    if n in (0,1):
        dp[n] = n
        return n
    if dp[n]==-1:

        dp[n] =fib_helper(n-1, dp)+fib_helper(n-2, dp)
    return dp[n]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
