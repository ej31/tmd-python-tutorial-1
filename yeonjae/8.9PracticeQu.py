# #연습문제1.리스트에서 홀수만 추출하기.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #주어진 리스트
odd_numbers = [] #for문과 if문을 사용하여 홀수만 추출하여 새로운 리스트 생성
for num in numbers:
    if num % 2 == 1:
        odd_numbers.append(num)
print(odd_numbers) #결과 출력, 출력값은 [1,3,5,7,9]




# #연습문제2. 1차원 리스트에서 최대/최소값 찾기
numbers = [5,2,8,4,1,9,6] #1차원 리스트
#힌트: for문과 if문을 사용하여 최댓값과 최솟값 찾기
max_value = numbers[0]  # 최댓값을 리스트의 첫 번째 원소로 초기화
min_value = numbers[0]  # 최솟값을 리스트의 첫 번째 원소로 초기화

for num in numbers:
    if num > max_value:
        max_value = num

    if num < min_value:
        min_value = num

print("최댓값:", max_value) #출력:최댓값:9
print("최솟값:", min_value) #출력:최솟값:1





# #연습문제3. 리스트 내 중복 제거하기.
fruit= ['apple', 'banana', 'orange', 'banana', 'kiwi', 'apple']
uique_fruit = [] #for문과 if문을 사용하여 중복 제거하기

for fruit_list in fruit:
    if fruit_list not in uique_fruit:
        uique_fruit.append(fruit_list)

print(uique_fruit) #출력: ['apple', 'banana', 'orange', 'kiwi']





# #연습문제4. 리스트에서 짝수와 홀수 분리하기
#for 문과 if문을 사용하여 짝수와 홀수 분리하기
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    elif num % 2 == 1:
        odd_numbers.append(num)

print("짝수", even_numbers)
print("홀수", odd_numbers)





# 연습문제5. 리스트의 모든 요소 곱하기
numbers = [1,2,3,4,5]
#for문을 이용하여 리스트의 모든 요소 곱하기
result = 1
for num in numbers:
    result = result*num

print("곱셈 결과:", result) #출력: 곱셈 결과:120





#연습문제6. 두 개의 리스트를 조합해 새로운 리스트 새성하기
names = ['Alice', 'Bob', 'Charlie']
scores = [80,90,78]
#zip 함수와 unpack을 사용하여 두 리스트 조합하기
combined_list = []
for g,h in zip(names, scores):
    combined_list.append([g,h])
print(combined_list) #출력: [['Alice', 85], ['Bob', 90], ['charlie', 78]]


