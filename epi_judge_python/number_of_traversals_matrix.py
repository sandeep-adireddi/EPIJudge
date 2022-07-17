from test_framework import generic_test


def number_of_ways(n: int, m: int) -> int:
    count_matrix = [[0]*m for _ in range(n)]
    count_matrix[0][0]=1
    for row in range(n):
        for col in range(m):
            top = left = 0
            if row-1>=0:
                top = count_matrix[row-1][col]
            if col-1>=0:
                left = count_matrix[row][col-1]
            count_matrix[row][col] += top+left
    return count_matrix[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
