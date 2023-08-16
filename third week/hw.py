#정수 리스트 받아서 그 중 짝수만 반환하기
def even_numbers(numbers):
    even = []
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
    return even

numbers = [1,2,3,4,5,6,7,8,9]
print(even_numbers(numbers))


#문자열을 입력받아 그 문자열을 거꾸로 뒤집은 결과를 반환하는 함수
def reverse_string(s):
    return s[::-1]
example_string = "파이썬"
print(reverse_string(example_string))


#리스트의 모든 요소를 더하는 함수
def sum_elements(elements):
    sum = 0
    for i in elements:
        sum += i
    return sum

numbers = [10,20,30,40,50]
print(sum_elements(numbers))


# 정수 리스트를 입력받아 그 중 가장 큰 수와 가장 작은 수를 반환하는 함수
def find_max_min(numbers):
    max_num = max(numbers)
    min_num = min(numbers)
    return min_num, max_num

numbers = [34,12,56,78,23]
print(find_max_min(numbers))


# 문자열을 입력받아 그 중 영어 모음의 개수를 반환하는 함수
def count_vowels(s):
    vowel_num = 0
    vowel_list = ('a','e','i','o','u','A','E','I','O','U')
    for i in s:
        if i in vowel_list:
            vowel_num += 1
    return vowel_num

string = "Hello, Python!"
print(count_vowels(string))


#문자열을 입력받아 각 알파벳 문자의 빈도를 사전 형태로 반환
def alphabet_frequency(s):
    frec_dict = {}
    for alpha in s:
        if alpha.isalpha():
            if alpha in frec_dict:
                frec_dict[alpha] += 1
            else:
                frec_dict[alpha] = 1
    return frec_dict

string = "Hello, Python!"
print(alphabet_frequency(string))