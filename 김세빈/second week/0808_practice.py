#문제 1번
#리스트에서 홀수만 추출하기
numbers_1 = [1,2,3,4,5,6,7,8,9,10]

odd_numbers = []
for i in numbers_1:
    if i % 2 != 0:
        odd_numbers.append(i)
print(odd_numbers)


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


#문제 3번
#리스트 내 중복 제거하기
fruits = ['apple','banana','orange','banana','kiwi','apple']
unique_fruits = []
for fruit in fruits:
    if fruit not in unique_fruits:
        unique_fruits.append(fruit)
print(unique_fruits)


#문제 4번
#리스트에서 짝홀수 분리하기
numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    elif num % 2 != 0:
        odd_numbers.append(num)
print(f"짝수: {even_numbers} \n홀수: {odd_numbers}")


#문제 5번
#리스트의 모든 요소 곱하기
numbers = [1,2,3,4,5]

result = 1
for i in numbers:
    result = result * numbers[i-1]
print(f"곱셈 결과: {result}")


#문제 6번
#두 개의 리스트를 조합하여 새로운 리스트 생성
names = ['Alice','Bob',"Charlie"]
scores = [85,90,78]
combined_list = list(zip(names, scores))

print(combined_list)