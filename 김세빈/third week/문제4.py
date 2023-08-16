# 정수 리스트를 입력받아 그 중 가장 큰 수와 가장 작은 수를 반환하는 함수
def find_max_min(numbers):
    max_num = max(numbers)
    min_num = min(numbers)
    return min_num, max_num

numbers = [34,12,56,78,23]
print(find_max_min(numbers))