from collections import defaultdict
from string import punctuation, whitespace

# list(int)에 관한 함수들


class AllNumberFuncitons:
    def __init__(self, numbers):
        self.__numbers = numbers

    def even_numbers(self):
        """
        짝수만 반환하는 함수
        """
        tmp = self.__numbers.copy()
        for number in tmp:
            if number % 2 == 0:
                continue
            elif number % 2 == 1:
                tmp.remove(number)
        return tmp

    def sum_elements(self):
        """
        값의 합을 반환하는 함수
        """
        return sum(self.__numbers)

    def find_max_min(self):
        """
        값의 최대최소를 tuple로 반환하는 함수
        """
        return (max(self.__numbers), min(self.__numbers))

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
        ans = 0
        for w in self.__string:
            if w.lower() in 'aeiou':
                ans += 1
        return ans

    def alphabet_frequency(self):
        """
        문자열을 입력받아 빈도를 사전 형태로 반환하는 함수
        """
        tmp_dict = defaultdict(int)
        for w in self.__string:
            if w not in punctuation and w not in whitespace:
                tmp_dict[w] += 1
        return tmp_dict


if __name__ == '__main__':
    print(AllNumberFuncitons(numbers=[1, 2, 3, 4, 5]).find_max_min())
    print(AllStringFunctions("Hello Python!").alphabet_frequency())
