#연습문제(1)
print('1부터 10까지의 짝수를 표시합니다.')
for i in range (1,11):
    if i%2 ==0:
        print(i)

#연습문제 (2)
print('1부터 10까지의 짝수를 표시합니다.')
for i in range(2,11,2):
    print(i)

#연습문제 (3) ctrl+/

for i in range (1,10):
    for j in range(1,10):
        result = i*j
        print(i*j, end='\t')
    print()

#첫번째 줄은 1*1, 1*2...
#두 번째 줄은 2*1, 2*2.....2*9이다.

#연습문제 (4)
for i in range(1,6):
    print('*'*i)

#연습문제(5)
for i in range(5,0,-1):
    print('*'*i)
