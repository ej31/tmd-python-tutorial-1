#정수 리스트 받아서 그 중 짝수만 반환하기
def even_numbers(numbers):
    even = []
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
    return even

numbers = [1,2,3,4,5,6,7,8,9]
print(even_numbers(numbers))