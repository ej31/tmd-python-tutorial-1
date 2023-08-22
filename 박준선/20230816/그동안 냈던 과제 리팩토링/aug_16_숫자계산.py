class Num_Utility:
    def __init__(self, numbers):
        self.__numbers = numbers

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
        max_num = min_num = self.__numbers[0]
        for i in self.__numbers:
            if i > max_num:
                max_num = i

        for j in self.__numbers:
            if j < min_num:
                min_num = j

        result = (max_num, min_num)
        return result

example1 = Num_Utility([33, 97, 24, 56, 81, 18, 22])
print(example1.find_max_min())
print(example1.odd_numbers())
print(example1.sum_element())
print(example1.multi_element())