from typing import List

from test_framework import generic_test
dp = []
def minimum_path_weight_helper(triangle,height,block_number):
    if height ==len(triangle)-1:
        dp[height][block_number] = triangle[height][block_number]
        return triangle[height][block_number]
   
    else:
        if dp[height][block_number]!=-1:
            return dp[height][block_number]
        else:
            dp[height][block_number] = (triangle[height][block_number]+
        min(minimum_path_weight_helper(triangle,height+1,block_number),
        minimum_path_weight_helper(triangle,height+1,block_number+1)))
        return dp[height][block_number]

def minimum_path_weight(triangle: List[List[int]]) -> int:
    if not triangle:
        return 0
    global dp
    dp = [[-1]*len(triangle[-1]) for _ in range(len(triangle[-1]))]
    minimum_path_weight_helper(triangle,0,0)
    
    
    return dp[0][0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'minimum_weight_path_in_a_triangle.py',
            'minimum_weight_path_in_a_triangle.tsv', minimum_path_weight))
