from test_framework import generic_test


def reverse(x: int) -> int:
    answer=0
    is_negative= False
    if x<0:
        is_negative=True
        x = -x

    while (x!=0):
        
        answer = answer*10+ x%10
        x//=10
    return -answer if is_negative else answer


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
