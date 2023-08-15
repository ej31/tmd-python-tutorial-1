# 20230809
# 1
numbers_type1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [number for number in numbers_type1 if number % 2 -1 == 0]
print(odd_numbers)

# 2
numbers_type2 = [5, 2, 8, 4, 1, 9, 6]
max_value = max(numbers_type2)
min_value = min(numbers_type2)

for num in numbers_type2:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

print("최댓값:", max_value)
print("최솟값:", min_value)

# 3
fruits = ['apple', 'banana', 'orange', 'banana', 'kiwi', 'apple']
unique_fruits = list(set(fruits))

for item in fruits:
    if item not in fruits:
        unique_fruits.append(item)

print(unique_fruits)

# 4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [number for number in numbers if number % 2 == 0]
odd_numbers = [number for number in numbers if number % 2 -1 == 0]

print("짝수:", even_numbers)
print("홀수:", odd_numbers)

# 5
numbers = [1, 2, 3, 4, 5]
result = 1
for num in numbers:
    result *= num
print("곱셈 결과:", result)

# 6
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]
zipped_list = zip(names, scores)
combined_list = list(zipped_list)
print(combined_list)




# 20230815
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
