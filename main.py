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












