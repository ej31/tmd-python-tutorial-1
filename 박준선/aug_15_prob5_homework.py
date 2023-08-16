# 5번문제 -------------------------------------------------------------------------------------------

def count_vowels(s):
    vowels = ["a", "e", "i", "o", "u", "y"]
    value = 0
    for i in s:
        if i in vowels:
            value += 1

    return value

string = "Hello, Python!"
print(count_vowels(string))