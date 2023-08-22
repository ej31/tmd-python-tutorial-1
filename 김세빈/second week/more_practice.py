#정삼각형 그리기
length = int(input("한변의 길이를 입력하세요: "))
for i in range(1, length + 1):
    print(" " * (length - i) + "*" * (2 * i - 1))

#역정삼각형 그리기
invert_lenght = int(input("한변의 길이를 입력하세요: "))
i = invert_lenght
while i >= 1:
    print(" " * (invert_lenght - i) + "*" * (2 * i - 1))
    i -= 1


#별 그리기
a = int(input('별의 길이를 입력해 주세요: '))
a_ = a
head = a // 13 * 5
body = a // 13 * 3
leg = a // 13 * 5

#머리
for num1 in range(1, head):
    print(" " * (a - num1) + "*" * (2 * num1 - 1))
#몸통
for num2 in range(1, body):
    print(" " * (a - a_) + "*" * (2 * a_ - 1))
    a_ -= 4
#다리
for num3 in range(leg,0,-1):
    temp = nm3
    print(" " * temp, end="")
    print("*" * num3 + " " * (a - num3 * 3) + "*" * num3)
    temp -= 1
