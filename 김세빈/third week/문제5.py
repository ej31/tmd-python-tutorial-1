# 문자열을 입력받아 그 중 영어 모음의 개수를 반환하는 함수
def count_vowels(s):
    vowel_num = 0
    vowel_list = ('a','e','i','o','u','A','E','I','O','U')
    for i in s:
        if i in vowel_list:
            vowel_num += 1
    return vowel_num

string = "Hello, Python!"
print(f"모음의 개수: {count_vowels(string)}")