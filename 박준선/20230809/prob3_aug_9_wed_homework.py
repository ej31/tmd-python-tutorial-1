# 3번문제 ------------------------------------------------------------
fruits = ["apple", "banana", "orange", "banana", "kiwi", "apple"]
unique_fruits = []
for fruit in fruits:
    if fruit not in unique_fruits:
        unique_fruits.append(fruit)

print(unique_fruits)