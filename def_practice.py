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

#2
def sum_elements(elements):
    total = sum(numbers)
    return total
numbers = [10, 20, 30, 40, 50]
total = sum_elements(numbers)
print(sum_elements(numbers))