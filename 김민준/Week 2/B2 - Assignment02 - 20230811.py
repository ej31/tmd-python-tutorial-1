# Assignment 02 - Find minimum and maximum

numbers = [5, 2, 8, 4, 1, 9, 6]

max_value = numbers[0]
min_value = numbers[0]

for i in numbers:
    if i > max_value:
        max_value = i
    elif i < min_value:
        min_value = i

print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
