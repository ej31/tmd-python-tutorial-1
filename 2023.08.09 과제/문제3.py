##3번##
#리스트 내 중복 제거하기
#마지막 결과 출력을 만족하는 코드를 채워 넣자

fruits = ['apple', 'banana', 'orange', 'banana', 'kiwi', 'apple']
unique_fruits = []

# 주어진 리스트를 순회하며 중복을 제거하여 유일한 과일만 unique_fruits에 추가
for fruit in fruits:
    if fruit not in unique_fruits:
        unique_fruits.append(fruit)

# 결과 출력
print(unique_fruits)
