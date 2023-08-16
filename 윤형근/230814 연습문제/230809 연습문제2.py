# 2 최댓값 최솟값 찾기

numbers = [5, 2, 8, 4, 1, 9, 6]

min_numbers = min(numbers)
max_numbers = max(numbers)

print("최댓값:", max_numbers)
print("최솟값:", min_numbers)


# 최댓값
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print("최댓값:", maximum)

# 최솟값

mimmum = numbers[0]
for num in numbers:
    if num < mimmum:
        mimmum = num
print("최솟값:", mimmum)