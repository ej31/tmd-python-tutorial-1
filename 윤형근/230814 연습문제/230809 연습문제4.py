# 4 홀수 짝수 분리하기

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [number for number in numbers if number % 2 ==0]
odd_numbers = [number for number in numbers if number % 2 ==1]

print("짝수:", even_numbers)
print("홀수:", odd_numbers)