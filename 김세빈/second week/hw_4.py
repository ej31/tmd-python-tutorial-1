#문제 4번
#리스트에서 짝홀수 분리하기
numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    elif num % 2 != 0:
        odd_numbers.append(num)
print(f"짝수: {even_numbers} \n홀수: {odd_numbers}")
