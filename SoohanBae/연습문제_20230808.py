# 문제 1번
print("1부터 10까지의 짝수를 표시합니다.")

for i in range(1, 11):
    if i % 2 == 0:
        print(i)


# 문제 2번
print("1부터 10까지의 짝수를 표시합니다.")

for i in range(2, 11, 2):
    print(i)


# 문제 3번
for i in range(1, 10):
    print(f"{i*1}\t{i*2}\t{i*3}\t{i*4}\t{i*5}\t{i*6}\t{i*7}\t{i*8}\t{i*9}")


# 문제 4번
for i in range(1, 6):
    print("*"*i)


# 문제 5번
for i in range(5, 0, -1):
    print("*"*i)


# n^2 by n^2 오각성 그리기
for i in range(3):
    print(" "*(10-i) + "*"*(2*i+1) + " "*(10-i))
for i in range(3):
    print(" "*(2*i) + "*"*(21-4*i) + " "*(2*i))
for i in range(3):
    print(" "*(4-i) + "*"*(5-2*i) + " "*(6*i+3) + "*"*(5-2*i) + " "*(4-i))
