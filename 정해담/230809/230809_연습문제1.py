# -*- coding: utf-8 -*-
"""230809_연습문제1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LN1lnMnwLDzc_dX3WQWgkCah2SjXVCVH

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

