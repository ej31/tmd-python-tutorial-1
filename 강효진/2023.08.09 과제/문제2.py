##2번##
#1차원 리스트에서 최대 / 최소값 찾기
#마지막 결과 출력을 만족하는 코드를 채워 넣자

# 1차원 리스트
numbers = [5, 2, 8, 4, 1, 9, 6]

# 초기 최대값과 최소값 설정
max_value = numbers[0]
min_value = numbers[0]

# 주어진 리스트를 순회하며 최대값과 최소값 찾기
for number in numbers:
    if number > max_value:
        max_value = number
    if number < min_value:
        min_value = number

# 결과 출력
print("최댓값:", max_value)
print("최소값:", min_value)