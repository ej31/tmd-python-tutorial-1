# Assignment 04 - Separate odd and even number from a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []
odd_numbers = []

for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)
    elif i % 2 != 0:
        odd_numbers.append(i)

print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")