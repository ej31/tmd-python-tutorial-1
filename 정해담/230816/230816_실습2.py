# -*- coding: utf-8 -*-
"""230816_실습2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LN1lnMnwLDzc_dX3WQWgkCah2SjXVCVH

##문자열을 입력받아서 그 문자열을 거꾸로 뒤집은 결과를 반환하는 함수를 완성해보자
"""

# 'reverse_string' 함수를 정의합니다.
#이 함수는 문자열을 입력받아 거꾸로 뒤집은 결과를 반환합니다.

def reverse_string(s):
  # 이 곳에 코드를 작성해주세요
  r_string = s[::-1]
  return r_string
  # 이 곳에 코드를 작성해주세요

# 예제로 사용할 문자열
example_string = "파이썬"
# 'reverse_string' 함수를 호출하고 결과를 출력합니다.
print(reverse_string(example_string)) # 출력: "썬이파"

