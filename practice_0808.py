# 예제 1
for i in range(1, 11):
    if i % 2 ==0:
        print(i)

# 예제 2
for x in range(2,11,2):
    print(x)

# 예제 3
for i in range(1, 10):
    print()
    for j in range(1, 10):
        print(i*j, end = '\t')

print('\t')

# 예제 4
for c in range(5):
	print((c+1) * "*")

# 예제 5
for d in range(5):
    for j in range(5):
        if j<d:
            print(" ", end=' ')
        else:
            print("*", end=' ')

print('\t')

# List 예제 1
numbers = [1,2,3,4,5,6,7,8,9,10]
odd_numbers = [num for num in numbers if num %2 ==1]
print(odd_numbers)

# List 예제 2
x = [5, 2, 8, 4, 1, 9, 6]
max_value = max(x)
min_value = min(x)
print("최대값", max_value)
print("최소값", min_value)

# List 예제 3
fruits = ['apple', 'banana', 'orange', 'banana', 'kiwi', 'apple']
unique_fruits = []
for f in fruits:
    if f not in unique_fruits:
        unique_fruits.append(f)
print(unique_fruits)

# List 예제 4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
odd_numbers = []
for num in numbers:
    if num %2 ==0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
print(even_numbers)
print(odd_numbers)


# List 예제 5
numbers = [1, 2, 3, 4, 5]
result = 1
for num in numbers:
    result *= num
print("곱셈 결과", result)

# List 예제 6
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]
combined_list = []

for name, score in zip(names, scores):
    combined_list.append([name, score])
print(combined_list)