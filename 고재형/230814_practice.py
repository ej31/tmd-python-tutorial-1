# 1번 문제
def even_numbers(n):
    even_list = []

    for num in n:
        if num % 2 == 0:
            even_list.append(num)
    return even_list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(even_numbers(numbers))

# 2번 문제

def reverse_string(s):
    _reverse_string = s[::-1]
    return _reverse_string

example_string = "파이썬"
print(reverse_string(example_string))

# 3번 문제

def sum_elements(elements):
    _elements = sum(elements)
    return _elements
numbers = [10, 20, 30, 40, 50]
print(sum_elements(numbers))



def sum_elements(elements):
    i = 0
    for _elements in elements:
        i += _elements
    return i
numbers = [10, 20, 30, 40, 50]
print(sum_elements(numbers))



# 4번 문제

def find_max_min(numbers):
    maximum = max(numbers)
    minimum = min(numbers)
    return maximum, minimum

numbers = [34, 12, 56, 78, 23]
print(find_max_min(numbers))

# 5번 문제

def count_vowels(s):
    vowels = 'aeiou'
    vowels += vowels.upper()
    vowel_count = 0
    for vowel in vowels:
        vowel_count += s.count(vowel)
    return vowel_count
string = "Hello, Python!"
print(count_vowels(string))

# 6번 문제

def alphabet_frequency(s):
    frequency = {}
    for alphabet in s:
        if alphabet.isalpha():
            if alphabet in frequency:
                frequency[alphabet] += 1
            else:
                frequency[alphabet] = 1
    return frequency
string = "Hello, Python!"
print(alphabet_frequency(string))


