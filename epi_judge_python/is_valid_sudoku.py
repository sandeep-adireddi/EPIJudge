from typing import List

from test_framework import generic_test

def has_duplicate(partial_assignment,start_row,end_row,start_col,end_col):
    is_present = [False]*10
    for i in range(start_row,end_row):
        for j in range(start_col,end_col):
            if partial_assignment[i][j]!=0 and  is_present[partial_assignment[i][j]]:
                return True
            is_present[partial_assignment[i][j]] = True
    return False
            
# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    for i in range(9):
        if has_duplicate(partial_assignment, i, i+1, 0, 9):
            return False
    for j in range(9):
        if has_duplicate(partial_assignment, 0, 9, j, j+1):
            return False
    size = 3
    for row in range(3):
        for col in range(3):
            if has_duplicate(partial_assignment, size*row, size*(row+1), size*col, size*(col+1)):
                return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
