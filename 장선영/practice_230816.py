# 실습_1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def even_numbers(numbers):
    even_numbers = []
    for i in numbers:
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers


print(even_numbers(numbers))


# 실습_2
def reverse_string(example_string):
    i = example_string[::-1]
    return i


example_string = "파이썬"
i = reverse_string(example_string)
print(reverse_string(example_string))

# 실습_3
numbers = [10, 20, 30, 40, 50]


def sum_elements(numbers):
    a = 0
    for b in numbers:
        a += b
    return a


print(sum_elements(numbers))

# 실습_4
numbers = [34, 12, 56, 78, 23]


def find_max_min(numbers):
    a = max(numbers)
    b = min(numbers)
    return a, b


print(find_max_min(numbers))

# 실습_5
string = "Hello, Python"


def count_vowls(s):
    vowls = "aeiouAEIOU"
    count = 0
    for i in string:
        if i in vowls:
            count += 1
    return count


print(count_vowls(string))

# 실습_6
string = "Hello, Python"


def alphabet_frequency(s):
    a = {}
    for i in s:
        if i.isalpha():
            i_lower = i.lower()
            if i_lower in a:
                a[i_lower] += 1
            else:
                a[i_lower] = 1
    return a


print(alphabet_frequency(string))
