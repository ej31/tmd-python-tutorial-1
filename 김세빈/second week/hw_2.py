#문제 2번
#1차원 리스트에서 최대/최소 값 찾기
numbers_2 = [5,2,8,4,1,9,6]

max_num = numbers_2[0]
min_num = numbers_2[0]

for i in numbers_2:
    if i > max_num:
        max_num = i
print(f"최대값은 {max_num}")

for j in numbers_2:
    if j < min_num:
        min_num = j
print(f"최소값은 {min_num}")
