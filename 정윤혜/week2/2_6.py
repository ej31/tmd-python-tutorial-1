# List 예제 6
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]
combined_list = []

for name, score in zip(names, scores):
    combined_list.append([name, score])
print(combined_list)