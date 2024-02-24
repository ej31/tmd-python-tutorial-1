##1번##
# 리스트에서 홀수만 추출하기
# 아래 주어진 리스트에서 (numbers 변수) 홀수만 포함 된 새로운 리스트 변수를 만들어보자

# 주어진 리스트
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 홀수만을 담을 빈 리스트 생성
odd_numbers = []

# 주어진 리스트를 순회하며 홀수를 추출하여 새 리스트에 추가
for number in numbers:
    if number % 2 == 1:
        odd_numbers.append(number)

# 결과 출력
print(odd_numbers)  # 출력값은 [1, 3, 5, 7, 9] 가 나와야 합니다