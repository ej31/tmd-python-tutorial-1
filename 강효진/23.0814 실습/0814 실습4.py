# 'find_max_min' 함수를 정의합니다.
# 이 함수는 정수 리스트를 입력받아 가장 큰 수와 가장 작은 수를 반환합니다.
def find_max_min(numbers):
    max_number = max(numbers)  # 리스트에서 가장 큰 수를 찾습니다.
    min_number = min(numbers)  # 리스트에서 가장 작은 수를 찾습니다.
    return max_number, min_number

# 예제로 사용할 정수 리스트
numbers = [34, 12, 56, 78, 23]

# 'find_max_min' 함수를 호출하고 결과를 출력합니다.
print(find_max_min(numbers))  # 출력: (78, 12)