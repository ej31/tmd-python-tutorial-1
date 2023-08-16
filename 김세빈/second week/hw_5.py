#문제 5번
#리스트의 모든 요소 곱하기
numbers = [1,2,3,4,5]

result = 1
for i in numbers:
    result = result * numbers[i-1]
print(f"곱셈 결과: {result}")
