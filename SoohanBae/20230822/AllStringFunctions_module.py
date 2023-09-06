from collections import defaultdict
from string import punctuation, whitespace

# 문자열에 관한 함수들


class AllStringFunctions:
    def __init__(self, string):
        self.__string = string

    def reverse_string(self):
        """
        string을 뒤집어 반환하는 함수
        """
        return self.__string[::-1]

    def count_vowels(self):
        """
        모음의 개수만 반환하는 함수
        """
        _ans = 0
        for w in self.__string:
            if w.lower() in 'aeiou':
                _ans += 1
        return _ans

    def alphabet_frequency(self):
        """
        문자열을 입력받아 빈도를 사전 형태로 반환하는 함수
        """
        _tmp_dict = defaultdict(int)
        for w in self.__string:
            if w not in punctuation and w not in whitespace:
                _tmp_dict[w] += 1
        return _tmp_dict
