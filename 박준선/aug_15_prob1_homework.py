# 1번문제 -------------------------------------------------------------------------------------------

def even_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(even_numbers(numbers))