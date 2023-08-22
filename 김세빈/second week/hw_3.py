#문제 3번
#리스트 내 중복 제거하기
fruits = ['apple','banana','orange','banana','kiwi','apple']
unique_fruits = []
for fruit in fruits:
    if fruit not in unique_fruits:
        unique_fruits.append(fruit)
print(unique_fruits)
