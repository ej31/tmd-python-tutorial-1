# 'alphabet_frequency' 함수를 정의합니다.
# 이 함수는 문자열을 입력받아 각 알파벳 문자의 빈도를 사전 형태로 반환합니다.
def alphabet_frequency(s):
    frequency = {}  # 알파벳 빈도를 저장할 사전

    for char in s:
        if char.isalpha():  # 알파벳 문자인 경우에만 처리합니다.
            char = char.lower()  # 대소문자 구분을 없애기 위해 소문자로 변환합니다.
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

    return frequency


# 예제로 사용할 문자열
string = "Hello, Python!"

# 'alphabet_frequency' 함수를 호출하고 결과를 출력합니다.
print(alphabet_frequency(string))  # 출력: {'h': 1, 'e': 1, 'l': 2, 'o': 2, 'p': 1, 'y': 1, 't': 1, 'n': 1}