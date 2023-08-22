class Utils:
    def __init__(self):
        pass

    @staticmethod
    def even_numbers(numbers):
        _numbers = []
        for number in numbers:
            if number % 2 == 0:
                _numbers.append(number)
        return _numbers

    @staticmethod
    def sum_elements(elements):
        return sum(elements)

    @staticmethod
    def find_max_min(numbers):
        found = []
        return max(numbers), min(numbers)

    @staticmethod
    def count_vowels(str):
        vowels = set("aeiouAEIOU")
        count = 0

        for char in str:
            if char in vowels:
                count += 1
        return count

    @staticmethod
    def alphabet_frequency(s):
        d = {}
        for char in s:
            if char not in d:
                d[char]= 1
            else:
                d[char]+= 1
        return d

