
# # 1번
print("1부터 10까지의 짝수를 표시합니다.")
for i in range(2,11,2):
    if i % 2 == 0:      # number % 2 == 0는 입력한 숫자를 2로 나눈 나머지가 0인지를 검사하는 조건
     print(i)



# 2번

print("1부터 10까지의 짝수를 표시합니다.")
for i in range(2,11,2):
    print(i)



# 3번

for i in range(1,10): # 왼쪽 피연산자(곱하는 수)를 1부터 9까지 반복
   for j in range(1,10): # 오른쪽 피연산자(곱해지는 수)를 1부터 9까지 반복
    result=i*j
    print(i*j ,end="\t")
   print()  # print()는 줄 바꿈



# 4번

for i in range(1, 6,+1):
    print('*'* i)

# 5번

for i in range(5,0 ,-1):
    print('*'* i)

