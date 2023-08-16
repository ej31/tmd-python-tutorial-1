# 2번문제 ------------------------------------------------------------------------
numbers = [5, 2, 8, 4, 1, 9, 6]
max_value = 0
min_value = 0

# 최댓값 구하기
for i in range(0, 7):
    if numbers[i] > max_value:
        max_value = numbers[i]
# 최솟값 구하기
for i in range(0, 7):
    if i == 0:
        min_value = numbers[i]
    if i > 0 and numbers[i] < min_value:
        min_value = numbers[i]

print("최댓값: ", max_value)
print("최솟값: ", min_value)