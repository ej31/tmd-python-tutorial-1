# Assignment 03 - Remove duplication inside List

fruits = ["apple", "banana", "orange", "banana", "kiwi", "apple"]
unique_fruits = []

for item in fruits:
    if item not in unique_fruits:
        unique_fruits.append(item)

print(f"Original fruits list: {fruits}")
print(f"List with duplicated removed: {unique_fruits}")