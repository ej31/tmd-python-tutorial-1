#문제 1번
#리스트에서 홀수만 추출하기
numbers_1 = [1,2,3,4,5,6,7,8,9,10]

odd_numbers = []
for i in numbers_1:
    if i % 2 != 0:
        odd_numbers.append(i)
print(odd_numbers)
