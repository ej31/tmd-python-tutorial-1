import random

def generate_two_random_numbers():
    random_number1 = random.randint(1, 9)
    random_number2 = random.randint(1, 9)
    return random_number1, random_number2

# 함수 호출하여 두 개의 랜덤 숫자 생성
random_num1, random_num2 = generate_two_random_numbers()
print("Random Number 1:", random_num1)
print("Random Number 2:", random_num2)