# 4번문제 ------------------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []
odd_numbers = []

for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)
    if i % 2 == 1:
        odd_numbers.append(i)

print("짝수:", even_numbers)
print("홀수:", odd_numbers)