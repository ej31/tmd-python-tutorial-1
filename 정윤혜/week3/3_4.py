#4
def count_vowels(_str):
    vowels = set("aeiouAEIOU")
    count = 0

    for char in _str:
        if char in vowels:
            count += 1
    return count

_str = "Hello, Python!"
print(count_vowels(_str))

#4-1
def count_vowels(_str):
    return sum(1 for char in _str if char.lower() in "aeiouAEIOU")
_str = "Hello, Python!"
print(count_vowels(_str))
