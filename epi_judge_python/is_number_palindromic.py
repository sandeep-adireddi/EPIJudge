from test_framework import generic_test
import math

def is_palindrome_number(x: int) -> bool:
    if (x<0):
        return False
    elif x==0:
        return True
    num_digit= math.floor(math.log10(x))+1
    mask = pow(10, num_digit-1)
    for i in range(num_digit//2):
        if (x%10!= x//mask):
            return False
        x %= mask
        x //=10
        mask//=100
    return True


    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
