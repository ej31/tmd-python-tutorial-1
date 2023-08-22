#if문과 for문을 사용하여 짝수 표시
print("1부터 10까지의 짝수를 표현합니다.")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

#for문만을 사용하여 짝수를 표시
print("1부터 10까지의 짝수를 표현합니다.")
for j in range(2,11,2):
    print(j)

#구구단 표를 출력
for num1 in range(1,10):
    for num2 in range(1, 10):
        multi = num1 * num2
        print(multi, end = '\t')
    print(end = '\n')

#별 출력 코드
star_1 = '*'
star_2 = '*'

for m in range(1,6):
    print(star_1 * m)
print('\n')
for k in range(5,0,-1):
    print(star_2 * k)
