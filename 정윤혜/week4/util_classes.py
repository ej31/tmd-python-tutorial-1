class Utils:
    def __init__(self):
        pass

    def even_numbers(numbers):
        _numbers = []
        for number in numbers:
            if number % 2 == 0:
                _numbers.append(number)
        return _numbers


    def sum_elements(elements):
        total = sum(elements)
        return total

    def find_max_min(numbers):
        found = []
        return max(numbers), min(numbers)

    def count_vowels(str):
        vowels = set("aeiouAEIOU")
        count = 0

        for char in str:
            if char in vowels:
                count += 1
        return count


    def alphabet_frequency(s):
        d = {}
        for char in s:
            if char not in d:
                d[char]= 1
            else:
                d[char]+= 1
        return d

