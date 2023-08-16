#리스트의 모든 요소를 더하는 함수
def sum_elements(elements):
    sum = 0
    for i in elements:
        sum += i
    return sum

numbers = [10,20,30,40,50]
print(sum_elements(numbers))