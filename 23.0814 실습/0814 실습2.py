# 'reverse_string' 함수를 정의합니다.
# 이 함수는 문자열을 입력받아 거꾸로 뒤집은 결과를 반환합니다.
def reverse_string(s):
    reversed_s = s[::-1]  # 문자열을 거꾸로 뒤집습니다.
    return reversed_s

# 예제로 사용할 문자열
example_string = "파이썬"

# 'reverse_string' 함수를 호출하고 결과를 출력합니다.
print(reverse_string(example_string))  # 출력: "썬이파"
