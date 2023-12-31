# -*- coding: utf-8 -*-
"""230816_실습6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LN1lnMnwLDzc_dX3WQWgkCah2SjXVCVH

##문자열을 입력 받아서 알파벳의 빈도를 반환하는 함수를 완성하세요
"""

# 'alphabet_frequency' 함수를 정의합니다.
#이 함수는 문자열을 입력받아 각 알파벳 문자의 빈도를 사전 형태로 반환합니다.
def alphabet_frequency(s):
  # 이 곳에 코드를 작성해주세요
  char_count = {}
  for char in s:
    if char.isalpha():
      if char in char_count:
        char_count[char] += 1
      else :
        char_count[char] = 1
  return char_count
  # 이 곳에 코드를 작성해주세요

# 예제로 사용할 문자열
string = "Hello, Python!"
# 'alphabet_frequency' 함수를 호출하고 결과를 출력합니다.
print(alphabet_frequency(string)) # 출력: {'H': 1, 'e': 1, 'l': 2, 'o': 2, 'P': 1, 'y': 1, 't': 1, 'h': 1, 'n': 1}

