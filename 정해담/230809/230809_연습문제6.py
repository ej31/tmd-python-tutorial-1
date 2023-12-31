# -*- coding: utf-8 -*-
"""230809_연습문제6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LN1lnMnwLDzc_dX3WQWgkCah2SjXVCVH

연습문제6. 두 개의 리스트를 조합해 새로운 리스트 생성하기
"""

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

