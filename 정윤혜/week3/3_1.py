#1
def even_numbers(numbers):
    _numbers = []
    for number in numbers:
        if number % 2 == 0:
            _numbers.append(number)
    return _numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
_numbers= even_numbers(numbers)
print(even_numbers(numbers))

#1-1
def even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
_numbers = even_numbers(numbers)
print(even_numbers(numbers))

#1-2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print(even_numbers)
