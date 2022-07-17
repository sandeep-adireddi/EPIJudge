from typing import List

from test_framework import generic_test


def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:
    is_visited = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (grid[row][col]==pattern[0] and is_pattern_contained_helper(grid,pattern,row,col,is_visited,0)):
                return True
    
    return False
def is_pattern_contained_helper(grid,pattern,row,col,is_visited,index):
    if index == len(pattern):
        return True
    if row<0 or row>=len(grid) or col<0 or col>=len(grid[0]) :
        return False
    if   grid[row][col]!=pattern[index]:
        return False
    if  grid[row][col]==pattern[index]:
        index+=1
    return (is_pattern_contained_helper(grid, pattern, row-1, col, is_visited, index) or
            is_pattern_contained_helper(grid, pattern, row+1, col, is_visited, index) or
            is_pattern_contained_helper(grid, pattern, row, col-1, is_visited, index) or
            is_pattern_contained_helper(grid, pattern, row, col+1, is_visited, index))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
