# List 예제 3
fruits = ['apple', 'banana', 'orange', 'banana', 'kiwi', 'apple']
unique_fruits = []
for f in fruits:
    if f not in unique_fruits:
        unique_fruits.append(f)
print(unique_fruits)