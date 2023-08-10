# 1번 문제

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = []
for _numbers in numbers:
    if _numbers % 2 == 1:
        odd_numbers.append(_numbers)
print(odd_numbers)

# 2번 문제

numbers = [5, 2, 8, 4, 1, 9, 6]
max_value = numbers[0]
min_value = numbers[0]
for _numbers in numbers:
    if max_value > _numbers:
        max_value = _numbers
    if min_value < _numbers:
        min_value = _numbers
print("최댓값 " + str(max_value))
print("최솟값", min_value)

# 3번 문제

fruits = ['banana', 'orange', 'banana', 'kiwi', 'apple','apple']
unique_fruit = []
for _fruit in fruits:
    if _fruit not in unique_fruit:
        unique_fruit.append(_fruit)
#unique_fruit_by_deepcopy = unique_fruit.copy()
#unique_fruit_by_deepcopy.sort()
#print(unique_fruit_by_deepcopy)
unique_fruit.sort()
print(unique_fruit)

# 4번 문제

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
odd_numbers = []
for _number in numbers:
    if _number % 2 == 0:
        even_numbers.append(_number)
    else:
        odd_numbers.append(_number)
print("짝수 :",  even_numbers)
print("홀수 : " + str(odd_numbers))

# 5번 문제

numbers = [1, 2, 3, 4, 5]
result = 1
for _number in numbers:
    result = _number * result
print("곱셈 결과:", result)


# 6번 문제

names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]
combined_list = []
for comb_list in zip(names, scores):
    combine_list = list(comb_list)
    combined_list.append(combine_list)
print(combined_list)









