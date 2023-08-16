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
