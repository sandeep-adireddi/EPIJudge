import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def decompose_into_dictionary_words(domain: str,
                                    dictionary: Set[str]) -> List[str]:
    index = 0
    decomposed_words=[]
    while(index<len(domain)):
        found_word = False
        for word in dictionary:
            if word == domain[index:index+len(word)]:
                
                found_word = True
                
                decomposed_words.append(word)
                
                index+=len(word)
                
                break
        if not found_word:
            return []
    return decomposed_words


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_decomposable_into_words.py',
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
