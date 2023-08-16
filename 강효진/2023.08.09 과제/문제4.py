##4번##
#리스트에서 짝수와 홀수 분리하기
#마지막 결과 출력을 만족하는 코드를 채워 넣자

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
odd_numbers = []

# 주어진 리스트를 순회하며 짝수와 홀수를 각각의 리스트에 분리하여 추가
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# 결과 출력
print("짝수:", even_numbers)
print("홀수:", odd_numbers)
