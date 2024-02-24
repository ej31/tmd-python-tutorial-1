# 4번문제 -------------------------------------------------------------------------------------------

# 첫번째 풀이 ---------------------------------------------------------------------------------------

def find_max_min(numbers):
    max_num = 0
    min_num = 0
    for i in numbers:
        if i > max_num:
            max_num = i

    for j in range(len(numbers)):
        if j == 0:
            min_num = numbers[j]
        if j > 0 and numbers[j] < min_num:
            min_num = numbers[j]

    result = (max_num, min_num)
    return result

numbers = [34, 12 ,56, 78, 23]
print(find_max_min(numbers))


# 두번째 풀이: 최솟값을 구하는 다른 아이디어 ------------------------------------------------------------

def find_max_min(numbers):
    max_num = 0
    min_num = 999999999999999999999999999999999999999
    for i in numbers:
        if i > max_num:
            max_num = i

    for j in numbers:
        if j < min_num:
            min_num = j

    result = (max_num, min_num)
    return result

numbers = [34, 12 ,56, 78, 23]
print(find_max_min(numbers))