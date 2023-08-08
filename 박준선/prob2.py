# 2번문제 최대값---------------------------------------------------

numbers = [5, 2, 8, 4, 1, 9, 6]
for i in range(0, 7):
    for t in range(i+1, 7):
        if numbers[i] < numbers[t]:
            break
        else:
            max_value = numbers[i]

print("최대값", max_value)

# 2번문제 최솟값----------------------------------------------------
numbers = [5, 2, 8, 4, 1, 9, 6]
for i in range(0,7):
    for t in range(i+1, 7):
        if numbers[i] > numbers[t]:
            break
        else:
            min_value = numbers[i]

print("최솟값", min_value)