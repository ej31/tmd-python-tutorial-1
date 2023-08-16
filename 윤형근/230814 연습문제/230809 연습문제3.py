# 3 리스트 내 중복 제거

fruits = ['apple', 'banana', 'orange', 'banana', 'kiwi', 'apple']

def remove_duplicates(fruits):
    unique_fruits =[]
    for element in fruits:
        if element not in unique_fruits:
            unique_fruits.append(element)
    return unique_fruits

unique_fruits = remove_duplicates(fruits)

print(unique_fruits)