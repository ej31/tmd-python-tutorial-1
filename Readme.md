# 연습문제 제출방법
1. 이 리포지토리를 Fork 합니다.
2. Fork 된 리포지토리에 본인 코드를 추가해서 Pull Request를 날리면 완료 입니다.
3. 파이썬 파일 하나당 문제는 하나만 포함 될 수 있도록 해주세요. 한 파일에 여러 문제가 섞여 있으면 보기가 어렵습니다.

## 참고
- 제출 된 PR을 통해 코드리뷰를 진행 할 수 있습니다. 코드리뷰 원하지 않는 경우 말씀해주세요.

#(1)
print("1부터 10까지의 짝수를 표시합니다.")
for 숫자 in range(1, 11):
    if 숫자 % 2 == 0:
        print(숫자)

#(2)
print("1부터 10까지의 짝수를 표시합니다.")
for 숫자 in range(2, 11, 2):
    print(숫자)

#(3)
for 행 in range(1, 10):
    for 열 in range(1, 10):
        결과 = 행 * 열
        print(결과, end='\t')
    print()

#(4)
for i in range(1, 6):
    print('*' * i)

#(5)
for i in range(5, 0, -1):
    print('*' * i)
