# 연습문제 (1)
print(f"연습문제 1-1")
print(f"1부터 10까지의 짝수를 표시합니다.")
i = 2
while i <= 10:
    print(i)
    i += 2

print(f"연습문제 1-2")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)