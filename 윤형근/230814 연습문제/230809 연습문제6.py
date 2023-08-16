# 6 리스트 생성

list_names = ['Alice', 'Bob', 'Charlie']
list_scores = [85, 90, 78]

zipped_list = zip(list_names, list_scores)

zipped_list_1 = list(zipped_list)

print(zipped_list_1)

for _names, _scores in zipped_list_1:
    print(_names, _scores)

combined_list = list(zip(list_names, list_scores))
print(combined_list)

