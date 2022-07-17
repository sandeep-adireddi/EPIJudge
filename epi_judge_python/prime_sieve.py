from typing import List
import math
from test_framework import generic_test



# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    prime_list = []
    is_prime = [True]*(n+1)
    is_prime[0] = is_prime[1] = False
    for p in range(2,n+1):
        if(is_prime[p]):
            prime_list.append(p)
            for i in range(p,n+1,p):
                is_prime[i] = False


    return prime_list


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
