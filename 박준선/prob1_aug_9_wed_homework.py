# 1번문제 ------------------------------------------------------------------

#for문 풀어서 코드짜기 ------------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = []
for i in numbers:
    if i % 2 == 1:
        odd_numbers.append(i)
print(odd_numbers)

# for문 한줄로 짜기 -------------------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [ i for i in numbers if i % 2 == 1]
print(odd_numbers)