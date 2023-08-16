# -*- coding: utf-8 -*-
"""연습문제.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mBcdq4NPXk0WvzL4BF73BjMeZ-Qw6qkF

연습문제1. 리스트에서 홀수만 추출하기
"""

#주어진 리스트
numbers = [1,2,3,4,5,6,7,8,9,10]

#for문과 if문을 사용하여 홀수만 추출하여 새로운 리스트 생성
odd_numbers = []

#이 사이에 코드를 채워보자


for i in numbers:
  if i%2 == 1:
    odd_numbers.append(i)


#이 사이에 코드를 채워보자

#결과 출력
print(odd_numbers)    #출력값은 [1,3,5,7,9]가 나와야 한다.

"""연습문제2. 일차원 리스트에서 최대/최소값 찾기"""

#1차원 리스트
numbers = [5, 2, 8, 4, 1, 9, 6]


#힌트 : for문과 if문을 사용하여 최댓값과 최솟값 찾기
#이 사이에 코드를 채워보자

sorted_numbers = sorted(numbers)
min_value = sorted_numbers[0]

sorted_numbers.reverse()
max_value = sorted_numbers[0]

#이 사이에 코드를 채워보자


#결과 출력
print("최댓값:", max_value)
print("최솟값:", min_value)

#1차원 리스트
numbers = [5, 2, 8, 4, 1, 9, 6]


#힌트 : for문과 if문을 사용하여 최댓값과 최솟값 찾기
#이 사이에 코드를 채워보자

max_value = numbers[0]
min_value = numbers[0]

for i in numbers:
  if i > max_value:
    max_value = i
  if i < min_value:
    min_value = i

#이 사이에 코드를 채워보자


#결과 출력
print("최댓값:", max_value)
print("최솟값:", min_value)

"""연습문제3. 리스트 내 중복 제거하기"""

fruits = ['apple', 'banana', 'orange', 'banana', 'kiwi', 'apple']

#for문과 if문을 사용하여 중복 제거하기
unique_fruits=[]


#이 사이에 코드를 채워보자

for i in fruits:
  if i not in unique_fruits:
    unique_fruits.append(i)

#이 사이에 코드를 채워보자


#결과출력
print(unique_fruits)    #출력 | ['apple', 'banana', 'orange', 'kiwi']

"""연습문제4. 리스트에서 짝수 홀수 구분하기"""

numbers = [1,2,3,4,5,6,7,8,9,10]

#for문과 if문을 사용하여 짝수와 홀수 분리하기
even_numbers=[]
odd_numbers=[]


#이 사이에 코드를 채워보자

for i in numbers:
  if i%2 == 0:
    even_numbers.append(i)
  else :
    odd_numbers.append(i)

#이 사이에 코드를 채워보자


#결과출력
print("짝수:", even_numbers)    #출력 | 짝수: [2, 4, 6, 8, 10]
print("홀수:", odd_numbers)     #출력 | 홀수 : [1, 3, 5, 7, 9]

"""연습문제5. 리스트의 모든 요소 곱하기"""

numbers = [1, 2, 3, 4, 5]

#for문을 사용하여 리스트의 모든 요소 곱하기
result=1


#이 사이에 코드를 채워보자

for i in numbers:
  result *= i

#이 사이에 코드를 채워보자


#결과 출력
print("곱셈결과:", result)    #출력 | 곱셈결과: 120

"""연습문제6. 두 개의 리스트를 조합해 새로운 리스트 생성하기"""

names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]

#zip()함수와 unpack을 사용하여 두 리스트 조합하기
combined_list = []


#이 사이에 코드를 채워보자

for a,b in zip(names, scores):
    combined_list.append([a,b])

#이 사이에 코드를 채워보자


#결과 출력
print(combined_list)    #출력 | [['Alice', 85], ['Bob', 90], ['Charlie', 78]]

