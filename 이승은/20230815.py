# 20230815 실습
# 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers
print(even_numbers(numbers))

# 2
def reverse_string(s):
    reverse_string = example_string[::-1]
    return reverse_string

example_string = "파이썬"
print(reverse_string(example_string))

# 3
def sum_elements(numbers):
    list_sum = sum(numbers)
    return list_sum

numbers = [10, 20, 30, 40, 50]
print(sum_elements(numbers))

# 4
def find_max_min(numbers):
    max_numbers = max(numbers)
    min_numbers = min(numbers)
    return max_numbers, min_numbers

numbers = [34, 12, 56, 78, 23]
print(find_max_min(numbers))

# 5
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count_vowels = string.count(vowels)
    count_vowels = sum(1 for char in string if char in vowels)
    return count_vowels

string = "Hello, Python!"
print(count_vowels(string))

# 6
def alphabet_frequency(s):
    alphabet_frequency= sum(1 for char in string if char.isalpha())
    return alphabet_frequency

string = "Hello, Python!"
print(alphabet_frequency(string))
