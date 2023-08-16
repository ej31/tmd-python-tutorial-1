# Assignment 05

def count_vowels(s):
    vowels = "AEIOUWYaeiouwy"
    vowel_count = 0

    for i in s:
        if i in vowels:
            vowel_count += 1

    return vowel_count


string = "Hello, Python!"

print(count_vowels(string))
