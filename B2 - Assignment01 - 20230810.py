# Assignment 01 - Extract odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = []

for i in numbers:
    if i % 2 == 0:
        continue
    elif i % 2 != 0:
        odd_numbers.append(i)

print(odd_numbers)