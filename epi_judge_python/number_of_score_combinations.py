from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    num_combinations_for_score = [[0]*(final_score+1) for _ in individual_play_scores]
    for index,play_score in enumerate(individual_play_scores):
        num_combinations_for_score[index][0]=1
        for score in range(1,final_score+1):
            if index<1:
                without_this_play =0
            else:
                without_this_play = num_combinations_for_score[index-1][score]
            if score<play_score:
                with_this_play = 0
            else:
                with_this_play = num_combinations_for_score[index][score-play_score]

            num_combinations_for_score[index][score] = with_this_play+without_this_play
        
    return num_combinations_for_score[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
