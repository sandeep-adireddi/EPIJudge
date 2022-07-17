from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    answer = ""
    is_negative =  ""
    if x<0:
        x = -x
        is_negative = "-"
    if x==0:
        return "0"
    while(x!=0):
        answer+= str(x%10)
        x//=10
    return is_negative+answer[::-1]


def string_to_int(s: str) -> int:
    # TODO - you fill in here.
    answer = 0
    is_negative = -1 if s[0]=='-' else 1
    if s[0]=="+" or s[0]=="-":
        s = s[1:]
    for char in s:
        answer*=10
        answer+=int(char)
    return answer*is_negative


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
