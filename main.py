#for문 사용하여 짝수
for i in range(2, 11, 2):
    print(i)
print()
#for문 if문 사용하여 짝수
a = int
for a in range(1, 11):
    if a % 2 == 0:
        print(a)
print()
# 구구단
for j in range(1, 10):
    for i in range(1, 10):
        print(f"{i * j}", end="\t")
    print()

#
for i in range(1, 5):
    for j in range(1, 4):
        a=int
        a = i + j
        if (a <= i):
            print("*")



for i in range(1, 5):
    spaces = " " * (a - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

for i in range(1, height + 1):
    stars = "*" * i
    print(stars)
