# 'sum_elements' 함수를 정의합니다.
# 이 함수는 리스트의 모든 요소를 더해 반환합니다.
def sum_elements(elements):
    total_sum = sum(elements)  # 리스트의 모든 요소를 더합니다.
    return total_sum

# 예제로 사용할 리스트
numbers = [10, 20, 30, 40, 50]

# 'sum_elements' 함수를 호출하고 결과를 출력합니다.
print(sum_elements(numbers))  # 출력: 150