# 5번

def count_vowels(s):
    count_vowels_1=0
    for string in s:
        if string in ["a", "e", "i", "o", "u"]:
           count_vowels_1 += 1

    return count_vowels_1       

string = "Hello, Python!"

print(count_vowels(string))