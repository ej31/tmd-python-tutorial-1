# 5 리스트 모든 요소 곱하기

numbers = [1, 2, 3, 4, 5]

multiply = 1 # 0이면 0곱하는거고 2면 2곱하는것임 1이 기본값

for number in numbers:
     multiply *= number
print(multiply)    