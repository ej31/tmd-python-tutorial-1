# 8월 15일 과제 하나로 묶기-------------------------------------------------------------------------------
from dataclasses import dataclass


@dataclass
class MaxMinDto:
    max_num : int
    min_num : int
class UsefulUtility:
    def __init__(self):
        pass



    def even_numbers(self, numbers):
        result = []
        for num in numbers:
            if num % 2 == 0:
                result.append(num)
        return result

    def odd_numbers(self, numbers):
        result = []
        for num in numbers:
            if num % 2 == 1:
                result.append(num)
        return result


    def reverse_string(self, string):
        return string[::-1]


    def sum_element(self, numbers):
        sum_result = 0
        for i in numbers:
            sum_result += i
        return sum_result

    def multi_element(self, numbers):
        multi_result = 1
        for i in numbers:
            multi_result *= i
        return multi_result


    def find_max_min(self, numbers):
        max_num = min_num = numbers[0]
        for i in numbers:
            if i > max_num:
                max_num = i
        for j in numbers:
            if j < min_num:
                min_num = j


        result = MaxMinDto(max_num = max_num, min_num = min_num)
        return result

    def count_vowels(self, string):
        vowels = ["a", "e", "i", "o", "u", "y"]
        value = 0
        for i in string:
            if i in vowels:
                value += 1
        return value

    def alphabet_frequency(self, string):
        final_dict = {}
        alpha_num = 0
        for i in string:
            if i.isalpha():
                alpha_num = string.count(i)
                final_dict[i] = alpha_num
        return final_dict









# example1 = UsefulUtility()
# print(example1.even_numbers([55, 22, 44, 88, 99, 11, 22, 77]))
# print(example1.odd_numbers([55, 22, 44, 88, 99, 11, 22, 77]))
# print(example1.reverse_string("every step i take, every move i make"))
# print(example1.sum_element([55, 22, 44, 88, 99, 11, 22, 77]))
# print(example1.multi_element([55, 22, 44, 88, 99, 11, 22, 77]))
# print(example1.find_max_min([55, 22, 44, 88, 99, 11, 22, 77]))
# print(example1.count_vowels("every step i take, every move i make"))
# print(example1.alphabet_frequency("every step i take, every move i make"))
















































































































































































