from test_framework import generic_test


def convert_to_base10(num_as_string,b1):
    string_to_int={
        "0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,
        "B":11,"C":12,"D":13,"E":14,"F":15
    }
    answer = 0
    multiplier = 1
    for char in num_as_string[::-1]:
        answer+= string_to_int[char]*multiplier
        multiplier*=b1
    return answer


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    is_negative = ""
    if num_as_string[0]=='-':
        num_as_string = num_as_string[1:]
        is_negative ="-"
    base_10_number = convert_to_base10(num_as_string, b1)
    hex_value_converter = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    answer=""
    multiplier = 1
    while True:
        digit = base_10_number%b2
        answer+= str(digit) if digit<10 else hex_value_converter[digit]
        base_10_number//=b2
        if base_10_number==0:
            break
    return is_negative+answer[::-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
