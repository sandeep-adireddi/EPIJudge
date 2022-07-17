from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    sign = -1 if( num1[0]<0) ^ (num2[0]<0) else 1
    num1[0],num2[0] = abs(num1[0]),abs(num2[0])
    answer = [0]*(len(num1)+len(num2))

    for i in range(len(num1)-1,-1,-1):
         for j in range(len(num2)-1,-1,-1):
            answer[i+j+1] += num1[i]*num2[j]
            answer[i+j] += answer[i+j+1]//10
            answer[i+j+1] = answer[i+j+1]%10
    i =0
    while( i<len(answer)-1 and answer[i]==0):
        i+=1
    answer = answer[i:]
    return [answer[0]*sign]+answer[1:] if i!=len(answer) else [0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
