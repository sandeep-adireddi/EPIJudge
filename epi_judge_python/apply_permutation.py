from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
    for i in range(len(A)):
        next_ = i
        while(perm[next_]>=0):
            temp = perm[next_]
            A[perm[next_]],A[i] = A[i],A[perm[next_]]
            perm[next_]=-1
            next_=temp

     

    # TODO - you fill in here.
    return


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
