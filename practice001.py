# 연습문제 1번 : 리스트에서 홀수만 추출하기
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)
print()
# 연습문제 2번 : 1차원 리스트에서 최대/최소 찾기
numbers = [5, 2, 8, 4, 1, 9, 6]
max_value = numbers[0]
min_value = numbers[0]

for num in numbers:
    if num > max_value:
        max_value = num
for num in numbers:
    if num < min_value:
        min_value = num

print("최대값:", max_value)
print("최솟값:", min_value)
print()
# 연습문제 3번 : 리스트 내 중복 제거
fruits = ['apple', 'banana', 'orange', 'banana', 'kiwi', 'apple']
unique_fruits = []
for g in fruits:
    if g not in unique_fruits:
        unique_fruits.append(g)
print(unique_fruits)
print()

# 연습문제 4번 : 리스트에서 짝수, 홀수 분리하기
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
print("짝수:", even_numbers)
print("홀수:", odd_numbers)
print()
# 연습문제 5번 : 리스트의 모든 요소 곱하기
numbers = [1, 2, 3, 4, 5]
result = 1
for num in numbers:
    result *= num
print("곱셈결과:", result)
print()
# 연습문제 6번 : 두 개의 리스트를 조합해 새로운 리스트 생성
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]
zipped = zip(names, scores)
combined_list = list(zipped)
print(combined_list)
print()

