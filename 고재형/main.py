# 1번 예제
print("1부터10까지의 짝수를 표시합니다")
for i in range(2,11):
    if i % 2 == 0:
        print(i)
        continue

# 2번 예제
for i in range(2,11,2):
    print(i)
# 3번 예제
for p in range(1,10):
    for o in range(1,10):
        result = o * p
        print(result, end = "\t")
    print()



# 4번 예제

for i in range(1, 6):
    print("*" * i)

# 5번 예제

for i in range(5, 0, -1):
    print("*" * i)



# 삼각형 만들기
for i in range(1,6):
    s = 5 - i
    t = 2 * i - 1
    print(" " * s + "*" * t)


# 역삼각형 만들기
for i in range(5, 0, -1):
    s = 5 - i
    t = i * 2 - 1
    print(" " * s + "*" * t)

# 연습
height = 5
for star in range(1, height):
    q = height - star
    w = star * 2
    e = height - star
    print("*" * q + " " * w + "*" * e)





