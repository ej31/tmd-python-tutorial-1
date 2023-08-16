# 3번문제 -------------------------------------------------------------------------------------------

def sum_element(elements):
    sum_result = 0
    for i in elements:
        sum_result += i

    return sum_result

numbers = [10, 20, 30, 40, 50]
print(sum_element(numbers))