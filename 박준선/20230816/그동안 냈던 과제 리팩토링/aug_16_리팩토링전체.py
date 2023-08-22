# 8월 15일 과제 하나로 묶기-------------------------------------------------------------------------------

class Useful_Utility:
    def __init__(self, numbers, string):
        self.__numbers = numbers
        self.__string = string


    def even_numbers(self):
        result = []
        for num in self.__numbers:
            if num % 2 == 0:
                result.append(num)
        return result

    def odd_numbers(self):
        result = []
        for num in self.__numbers:
            if num % 2 == 1:
                result.append(num)
        return result


    def reverse_string(self):
        rever_str = self.__string[::-1]
        return rever_str


    def sum_element(self):
        sum_result = 0
        for i in self.__numbers:
            sum_result += i
        return sum_result

    def multi_element(self):
        multi_result = 1
        for i in self.__numbers:
            multi_result *= i
        return multi_result


    def find_max_min(self):
        max_num = 0
        min_num = 99999999
        for i in self.__numbers:
            if i > max_num:
                max_num = i
        for j in self.__numbers:
            if j < min_num:
                min_num = j
        result = (max_num, min_num)
        return result

    def count_vowels(self):
        vowels = ["a", "e", "i", "o", "u", "y"]
        value = 0
        for i in self.__string:
            if i in vowels:
                value += 1
        return value

    def alphabet_frequency(self):
        final_dict = {}
        alpha_num = 0
        for i in self.__string:
            if i.isalpha() == True:
                alpha_num = self.__string.count(i)
                final_dict[i] = alpha_num
        return final_dict


example1 = Useful_Utility([10, 21, 30, 40, 57, 60, 73], "hello world")
print(example1.reverse_string())
print(example1.alphabet_frequency())
print(example1.find_max_min())
print(example1.odd_numbers())
print(example1.multi_element())


























































































































































































