from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    LENGTH_A = len(A)
    LENGTH_B = len(B)

    distance_matrix = [[0]*(LENGTH_B+1) for _ in range(LENGTH_A+1)]

    for i in range(1,LENGTH_B+1):
        
            distance_matrix[0][i] = i
        
    for i in range(1,LENGTH_A+1):
        
            distance_matrix[i][0] =  i
        
    for row in range(1,LENGTH_A+1):
        for col in range(1,LENGTH_B+1):
            if A[row-1]==B[col-1]:
                distance_matrix[row][col] = distance_matrix[row-1][col-1]
            else:
                distance_matrix[row][col] = 1+min( [distance_matrix[row-1][col],
                                                    distance_matrix[row-1][col-1],
                                                    distance_matrix[row][col-1]])
        
    return distance_matrix[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
