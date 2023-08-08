# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# print("hello world")
# # 여기는 읽지 않습니다..무시해요
# # this_is_variable = 10
# # print(this_is_variable)
# # print(this_is_variable)
# # print(this_is_variable)
#
# # print(this_is_variable)
# # print(this_is_variable)
# # print(this_is_variable)
# # print(this_is_variable)
# # print(this_is_variable)
#
# print("dsfadsfa'''''")
# print('sdfklsdf""""')
#
# # TODO hgghghjfdgbkjhdgfsklj
# print("""sdfdsf
# sdfsdf
# dfggfd
# vcbvcb
# dfb""")
# """fdagfdagfda"""
# 123
#
# this_is_variable = 10 # 스네이크
# second_this_is_variable = 20
#
# print("this_is_variable 변수는 ..", this_is_variable, "입니다.")
# print(f"this_is_variable 변수는 .. {this_is_variable} 입니다.")
#
# declaration_variable = 10
# print(declaration_variable)
#
# declaration_variable = 20
# print(eval("1+2"))
# print(1+2)
#
# num1 = 10
# num2 = 20
# print(eval("num1 + num2"))
# print(num1 + num2)
#
# print(f"나는 숫자 {num1} 이고, 나한테 10을 더하면 {num2}이다.")
#
# a = 2
# b = 4

# --------------------------------------------------

# 8월 7일 월요일 배운거 연습
# print("int_variable_\"12\"3")
# print("""int_variable_me
# int_variable
# sadjkv
# akldvn""")
#
# this_is_integer_variable = 123
# this_is_string_variable = "Genius"
#
# print(f"this_is_integer_variable 변수값은 {this_is_integer_variable}입니다")
# print(f"this_is_string_variable 변수값은 {this_is_string_variable}입니다.")
#
# num1 = 10
# num2 = 20
# result = num1 + num2
# print(result)
#
# num1 = 10
# num2 = 20
# result = num1*num2
# print(result)
#
# # is_sunny = True
# # is_raining = False
# #
# # if is_sunny:
#
# # 불리언 변수 선언
# is_sunny = True
# is_raining = False
#
# # 조건문 사용
# # if is_sunny:
# #     print("날씨가 화창합니다.")
# # else:
# #     print("날씨가 비옵니다.")
#
# # 논리 연산자 사용
# # temperature = 25
# # is_warm = temperature > 20
# # if is_warm and not is_raining:
# #     print("날씨가 따뜻하고 비가 오지 않습니다.")
# temperature = 27
# is_warm = temperature > 20
#
# if is_warm and not is_raining:
#     print("날씨가 따듯하고 비가 오지 않습니다.")
#
# x = True
# y = False
#
# result = x and y
# print(result)
#
# result = x or y
# print(result)
#
# x = 20
# y = 30
# result = "x가 보다 큽니다." if x > y else "y가 x보다 큽니다."
# print(result)
#
# # eval() 함수의 기본 개념과 용도 예제
#
# # 1. eval() 함수는 문자열을 파이썬 코드로 실행하는 함수입니다.
# # 2. 주로 수식 계산, 변수 값 대입, 간단한 코드 실행에 사용됩니다.
# # 3. eval()은 주어진 문자열을 해석하고 해당 결과를 반환합니다.
#
# # 예제 1: 수식 계산
# expression = "3 + 5 * 2"
# result = eval(expression)
# print(f"수식 '{expression}'의 결과: {result}")
#
# # 예제 2: 변수 값 대입 및 출력
# x = 10
# y = 5
# expression = "x + y"
# result = eval(expression)
# print(f"변수 값 대입 후 수식 '{expression}'의 결과: {result}")
#
# def aver(num1: int, num2: int):
#     print(f"num1 is {num1}, num2 is {num2}")
#     result = (num1 + num2)/2
#     return result
#
# practice = aver(20, 30)
# print(practice)
#
# squares = [x**2 for x in range(1, 11)]
# print(squares)
#
# name = "박준선"
# age = 30
# introduce = f"나의 이름은 {name}입니다. 그리고 저의 나이는 {age}살 입니다."
# print(introduce)
#
# # eval함수 연습
# sen = "1+3*(2+7)"
# result = eval(sen)
# print(f"{sen}의 계산결과는 {result}입니다.")
#
# is_true1 = True
# is_true2 = True
# is_false1 = False
# is_false2 = False
# result = is_false2 or is_false1
# print(result)
#
# x = 50
# y = 35
# result = "x가 y보다 크다" if x>y else "y가 x보다 크다"
# print(result)
#
# squares = [x**3 for x in range(1, 11)]
# print(squares)
#
# # x**3 - y**2 을 계산하는 sen 함수 만들기
#
# def sen(x: int, y: int):
#     practice = x**3 - y**2
#     print(f"x is {x}, y is {y}")
#     #result = print(f"x^3 - y^2 은 {practice}이다" )
#     return practice
#
# asdf = sen(15, 25)
# print(asdf)
#
#
#
# list1 = [(x**3-100) for x in range(5, 14)]
# print(list1)
#
# variable_1 = 20
# str_1 = "스트링"
#
# print(f"숫자는 {variable_1}이고 문자는 {str_1}입니다.")
#
# temperature = 17
# weather = "날씨가 화창합니다." if temperature > 20 else "날씨가 춥습니다."
# print(weather)
#
# def oper(x: int, y: int, z: int):
#     print(f"x is {x}, y is {y}, z is {z}")
#     result = x*y - z
#     return result
# pratice = oper(3, 5, 7)
# print(pratice)
#
# squares = [ x**2 for x in range(11,15) ]
# print(squares)
#
# x = 7
# x += 3
# print(x)
#
# x = 7
# x *= 3
# print(x)
#
# x = 7
# x -= 3
# print(x)
#
# x = 9
# x /= 3
# print(x)
#
# x = 17
# x //= 3
# print(x)
#
# x = 7
# x %= 3
# print(x)
#
# x = 7
# x **= 2
# print(x)
#
# list = [1, 2, 3, 4, 5]
# del list[2]
# print(list)
#
# list = [1, 2, 3, 4, 5]
# list.remove(3)
# print(list)
#
# list = [1, 2, 3, 4, 5]
# remove_element = list.pop(2)
# print(list)
# print(remove_element)
#
# list_1 = [1, 2, 3, 4, 5]
# list_2 = list_1
# print(f"변경전 리스트1 = {list_1}, 변경전 리스트2 = {list_2}")
# list_2[0] = 10
# print(f"변경후 리스트1 = {list_1}, 변경후 리스트2 = {list_2}")
#
# list_1 = [1, 2, 3, 4, 5]
# list_2 = list_1.copy()
# print(f"변경전 리스트1 = {list_1}, 변경전 리스트2 = {list_2}")
# list_2[0] = 10
# print(f"변경후 리스트1 = {list_1}, 변경후 리스트2 = {list_2}")
# print(list_2[0])
# print(list_2[1:4])
# for asdf in list_2:
#     print(asdf)

# fruits = ["apple", "orange", "grape"]
# for fruit in fruits:
#     print(fruit)

# squares = []
# for x in range(1,6):
#     squares.append(x**3)
# print(squares)

# square = [num**3 for num in range(1, 6)]
# print(square)

# -------------------------------------------------------------------------------------------
# 8월 8일 수업

x = 10
if x > 0:
    print("x는 양수")
elif x < 0:
    print("x는 음수")
else:
    print("x는 0")

# case3
# score = int(input("시험점수 입력하세요"))
#
# if score >= 90:
#     print("학점 A")
# elif score >= 80:
#     print("학점 B")
# elif score >= 70:
#     print("학점 C")
# else:
#     print("학점은 0!")

# list_month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#
# month = 99
# for _month in list_month:
#     print(" 반복시작 ")
#     print(f"현재 몇월인가요 -- {_month}")
#     print("반복종료")
#
# print(f"for문 바깥에서 month 변수의 상태 -- {month}")

# just_txt = "HelloWorld!"
#
# for txt in just_txt:
#     print(txt)

# i = 0
# while i <= 5:
#     print(f"i의 현재값은 .. {i}")
#     i += 1
#
# break_cnt = 0
# while True:
#     if break_cnt > 5:
#         break
#     print(f"현재 break_cnt 값은...{break_cnt}")
#     break_cnt += 1

# ------------------첫번째 문제
print("1부터 10까지의 짝수를 표시합니다.")
for i in range(1, 6):
    print(i*2)
    if i == 5:
        break

# ------------------두번째 문제
print("1부터 10까지 짝수를 표기합니다.")
for i in range(2, 11, 2):
    print(i)


# ---------------------- 세번쨰문제
# int = [x for x in range(1, 10)]
# print(int)

# ----------------------네번째문제
# 99단
for i in range(1, 10):
    int = i
    for t in range(1,10):
        int_2 = int * t
        print(int_2, end= '\t')
        if t == 9:
            print()

# 삼각형 문제
for i in range(1, 6):
    print("*" * i)

# 역삼각형 문제
for i in range(1, 6):
    star = "*****"
    print(star[i-1:5])

# 리스트
this_is_list = ["hello", "world", "hi", "three", "four", "five"]