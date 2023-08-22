#4
def count_vowels(str):
    vowels = set("aeiouAEIOU")
    count = 0

    for char in str:
        if char in vowels:
            count += 1
    return count

str = "Hello, Python!"
print(count_vowels(str))