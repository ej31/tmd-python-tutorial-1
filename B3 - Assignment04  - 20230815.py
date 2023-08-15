# Assignment 04

def find_min_max(numbers):
    Max = 0
    Min = 0

    for i in numbers:
        temp = 0
        if i > Max:
            Max = i
        elif i < Max:
            continue

    for j in numbers:
        if j < Min:
            Min = j
        elif Min == 0:
            Min = j

    return Max, Min


numbers = [14, 12, 56, 78, 23]

print(find_min_max(numbers))
