
# 4번

numbers = [34, 12, 56, 78, 23]

def find_max_min(numbers):
    max_number = numbers[0]
    min_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
        if number < min_number:
            min_number = number
    return max_number, min_number


print(find_max_min(numbers))


