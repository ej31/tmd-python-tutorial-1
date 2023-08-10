# 연습문제

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
