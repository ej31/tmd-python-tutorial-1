#실습1. 정수 리스트를 입력받아, 그 중 짝수만을 반환하는 함수 코드

#'even_numbers' 함수를 정의합니다.
#이 함수는 정수 리스트를 입력받아 짝수만을 반환합니다.

def even_numbers(numbers):
    even_list=[] #짝수를 저장할 리스트 생성
    for putt in numbers:
        if putt %2 ==0:
            even_list.append(putt) #even_list에 putt에 있는 숫자를 넣어줘
    return even_list

#예제로 사용할 숫자 리스트
numbers = [1,2,3,4,5,6,7,8,9]
#'even_numbers' 함수를 호출하고 결과를 출력합니다.
print(even_numbers(numbers))



#실습2. 문자열을 입력받아서 그 문자열을 거꾸로 뒤집은 결과를 반환하는 함수를 완성
#'reverse_string'함수를 정의한다.
#이 함수는 문자열을 입력받아 거꾸로 뒤집은 결과를 반환한다.

def reverse_string(s):
    reverse_txt = ''
    for str_reverse in s:
        reverse_txt = str_reverse + reverse_txt
    return reverse_txt

#예제로 사용할 문자열
example_string = "파이썬"

#reverse_string 함수를 호출하고 결과를 출력한다.
print(reverse_string(example_string))



#3. 리스트의 모든 요소를 더하는 함수를 완성해보자.
#sum_elements'함수를 정의한다.
#이 함수는 리스트의 모든 요소를 더해 반환한다.
def sum_elements(elements):
    s=0
    for each_elements in elements:
        s+= each_elements
    return s
#예제로 사용할 리스트
numbers = [10,20,30,40,50]
#sum_elements' 함수를 호출하고 결과를 출력한다.
print(sum_elements(numbers)) #출력:150

#실습4. 정수 리스트를 입력받아 그 중 가장 큰 수와 가장 작은 수를 반환하는 함수
def find_max_min(numbers):
    max_num = min_num = numbers[0]
    for i in numbers:
        if i < min_num:
            min_num = i
        elif i > max_num:
            max_num = i
    return max_num,min_num

#예제로 사용할 정수 리스트
numbers = [34,12,56,78,23]

#'find_max_min'함수를 호출하고 결과를 출력합니다.
print(find_max_min((numbers))) #출력: (78,12)

#실습5. 문자열을 입력 받아서 그 중 영어 모음의 개수를 반환하는 함수를 완성
#'count_vowels' 함수를 정의합니다.
#이 함수는 문자열을 입력받아 모든 모음의 개수를 반환합니다.
# 'count_vowels' 함수를 정의합니다.
# 이 함수는 문자열을 입력받아 모든 모음의 개수를 반환합니다.
def count_vowels(s):
    vowels = "aeiou"  # 모음을 저장한 문자열
    vowel_count = 0  # 모음 개수를 저장할 변수 초기화

    for char in s:
        if char in vowels:
            vowel_count += 1  # 모음일 경우 개수 증가

    return vowel_count  # 모음 개수 반환


# 예제로 사용할 문자열
string = "Hello, Python!"
# 'count_vowels' 함수를 호출하고 결과를 출력합니다.
print(count_vowels(string))  # 출력: 4


# 'alphabet_frequency' 함수를 정의합니다.
# 이 함수는 문자열을 입력받아 각 알파벳 문자의 빈도를 사전 형태로 반환합니다.
def alphabet_frequency(s):
    frequency = {}  # 알파벳 빈도를 저장할 사전 생성
    for char in s:
        if char.isalpha():  # 알파벳인 경우에만 처리
            if char in frequency:
                frequency[char] += 1  # 이미 있는 알파벳일 경우 빈도 증가
            else:
                frequency[char] = 1  # 처음 나온 알파벳일 경우 빈도 초기화

    return frequency  # 알파벳 빈도 사전 반환
# 예제로 사용할 문자열
string = "Hello, Python!"
# 'alphabet_frequency' 함수를 호출하고 결과를 출력합니다.
print(alphabet_frequency(string))


