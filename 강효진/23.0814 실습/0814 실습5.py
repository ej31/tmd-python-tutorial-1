# 'count_vowels' 함수를 정의합니다.
# 이 함수는 문자열을 입력받아 모든 모음의 개수를 반환합니다.
def count_vowels(s):
    vowels = "aeiouAEIOU"  # 영어 모음 문자들을 저장한 문자열

    vowel_count = 0  # 모음 개수를 세기 위한 변수

    for char in s:
        if char in vowels:  # 문자가 모음 문자인지 확인합니다.
            vowel_count += 1  # 모음 개수를 증가시킵니다.

    return vowel_count


# 예제로 사용할 문자열
string = "Hello, Python!"

# 'count_vowels' 함수를 호출하고 결과를 출력합니다.
print(count_vowels(string))  # 출력: 4