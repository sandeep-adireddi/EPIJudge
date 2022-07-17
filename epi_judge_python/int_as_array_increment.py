from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    carry = 1
    index = len(A)-1
    while (carry!=0 and index!=0):
        A[index]+=carry
        carry =0
        if A[index]==10:
            A[index] =0
            carry =1
        index-=1
    if carry==1:
        if A[0]+carry==10:
            A[0] =0
            A.insert(0, 1)
        else:
            A[0]+=carry
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
