# 6번문제 -----------------------------------------------------------
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]

zipped_list = zip(names, scores)
listed = list(zipped_list)
combined_list = []
for name, score in listed:
    combined_list.append([name, score])

print(combined_list)