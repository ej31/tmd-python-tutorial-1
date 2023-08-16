# Assignment 01

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even_numbers(numbers):
    even_list = []
    for i in numbers:
        if i % 2 == 0:
            even_list.append(i)

    return even_list

print(even_numbers(numbers))
