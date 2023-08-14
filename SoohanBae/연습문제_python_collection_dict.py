# 'even_numbers' 함수를 정의합니다.
# 이 함수는 정수 리스트를 입력받아 짝수만을 반환합니다.
def even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            continue
        elif number % 2 == 1:
            numbers.remove(number)
    return numbers


# 이 곳에 코드를 작성해주세요
# 이 곳에 코드를 작성해주세요
# 예제로 사용할 숫자 리스트
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 'even_numbers' 함수를 호출하고 결과를 출력합니다.
print(even_numbers(numbers))  # 출력: [2, 4, 6, 8]


# 'reverse_string' 함수를 정의합니다.
# 이 함수는 문자열을 입력받아 거꾸로 뒤집은 결과를 반환합니다.
def reverse_string(s):
    return s[::-1]


# 예제로 사용할 문자열
example_string = "파이썬"
# 'reverse_string' 함수를 호출하고 결과를 출력합니다.
print(reverse_string(example_string))  # 출력: "썬이파"

# 'sum_elements' 함수를 정의합니다.
# 이 함수는 리스트의 모든 요소를 더해 반환합니다.


def sum_elements(elements):
    return sum(numbers)


# 예제로 사용할 리스트
numbers = [10, 20, 30, 40, 50]
# 'sum_elements' 함수를 호출하고 결과를 출력합니다.
print(sum_elements(numbers))  # 출력: 150


# 'find_max_min' 함수를 정의합니다.
# 이 함수는 정수 리스트를 입력받아 가장 큰 수와 가장 작은 수를 반환합니다.
def find_max_min(numbers):
    return (max(numbers), min(numbers))


    # 이 곳에 코드를 작성해주세요
    # 이 곳에 코드를 작성해주세요
    # 예제로 사용할 정수 리스트
numbers = [34, 12, 56, 78, 23]
# 'find_max_min' 함수를 호출하고 결과를 출력합니다.
print(find_max_min(numbers))  # 출력: (78, 12)


# 'count_vowels' 함수를 정의합니다.
# 이 함수는 문자열을 입력받아 모든 모음의 개수를 반환합니다.
def count_vowels(s):
    ans = 0
    for w in s:
        if w.lower() in 'aeiou':
            ans += 1
    return ans


# 예제로 사용할 문자열
string = "Hello, Python!"
# 'count_vowels' 함수를 호출하고 결과를 출력합니다.
print(count_vowels(string))  # 출력: 4


# 'alphabet_frequency' 함수를 정의합니다.
# 이 함수는 문자열을 입력받아 각 알파벳 문자의 빈도를 사전 형태로 반환합니다.
def alphabet_frequency(s):
    from collections import defaultdict
    tmp_dict = defaultdict(int)
    for w in s:
        tmp_dict[w] += 1
    return tmp_dict


# 이 곳에 코드를 작성해주세요
# 이 곳에 코드를 작성해주세요
# 예제로 사용할 문자열
string = "Hello, Python!"
# 'alphabet_frequency' 함수를 호출하고 결과를 출력합니다.
# 출력: {'H': 1, 'e': 1, 'l': 2, 'o': 2, 'P': 1, 'y': 1, 't': 1, 'h': 1, 'n': 1}
print(alphabet_frequency(string))
