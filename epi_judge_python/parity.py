from test_framework import generic_test


def parity(x: int) -> int:
    '''
    solution one:
    ones_count = 0
    while (x!=0):
        ones_count+= x & 1
        x = x>>1
    return int(ones_count%2!=0)'''
    x^= x>>32
    x^= x>>16
    x^= x>>8
    x^= x>>4
    x^= x>>2
    x^=x>>1
    return x & 1




if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
