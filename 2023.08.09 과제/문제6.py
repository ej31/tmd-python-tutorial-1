##6번##
#두 개의 리스트를 조합해 새로운 리스트 생성하기
#마지막 결과 출력을 만족하는 코드를 채워 넣자

names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]

combined_list = []

# 두 개의 리스트를 조합하여 새로운 리스트 생성
for name, score in zip(names, scores):
    combined_list.append([name, score])

# 결과 출력
print(combined_list)