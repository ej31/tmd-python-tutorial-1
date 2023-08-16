from enum import unique


print("리스트 1번 문제")
numbers = [i for i in range(1, 11)]

odd_numbers = [number for number in numbers if number % 2 == 1]


print(odd_numbers)

print("\n")
print("리스트 2번 문제")

numbers = [5, 2, 8, 4, 1, 9, 6]
max_value = 0
min_value = 100

for number in numbers:
    if number >= max_value:
        max_value = number

    if number <= min_value:
        min_value = number

print("최댓값: ", max_value)
print("최솟값: ", min_value)


print("\n")
print("리스트 3번 문제")

fruits = ['apple', 'banana', 'orange', 'banana', 'kiwi', 'apple']

unique_fruits = []

for fruit in fruits:
    if fruit not in unique_fruits:
        unique_fruits.append(fruit)

print(unique_fruits)


print("\n")
print("리스트 4번 문제")

numbers = [i for i in range(1, 11)]

even_numbers = [number for number in numbers if number % 2 == 0]
odd_numbers = [number for number in numbers if number % 2 == 1]

print("짝수: ", even_numbers)
print("홀수: ", odd_numbers)


print("\n")
print("리스트 5번 문제")

numbers = [1, 2, 3, 4, 5]

result = 1

for number in numbers:
    result *= number

print("곱셈 결과:", result)

print("\n")
print("리스트 6번 문제")

names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]

combined_list = list(map(list, zip(names, scores)))

print(combined_list)
