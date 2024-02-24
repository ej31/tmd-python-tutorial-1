# 'even_numbers' 함수를 정의합니다.
# 이 함수는 정수 리스트를 입력받아 짝수만을 반환합니다.
def even_numbers(numbers):
    # 짝수를 저장할 리스트를 생성합니다.
    even_list = []

    # 주어진 숫자 리스트를 순회하면서 짝수인 경우만 저장합니다.
    for number in numbers:
        if number % 2 == 0:  # 숫자가 짝수인지 확인합니다.
            even_list.append(number)  # 짝수를 리스트에 추가합니다.

    return even_list  # 짝수 리스트를 반환합니다.


# 예제로 사용할 숫자 리스트
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 'even_numbers' 함수를 호출하고 결과를 출력합니다.
print(even_numbers(numbers))  # 출력: [2, 4, 6, 8]