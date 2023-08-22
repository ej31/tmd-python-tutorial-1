#5
def alphabet_frequency(s):
    d = {}
    for char in s:
        if char not in d:
            d[char]= 1
        else:
            d[char]+= 1
    return d
string = "Hello, Python!"
print(alphabet_frequency(string))

#5-1
def alphabet_frequency(s):
    d = {}
    for char in s:
        if char.isalpha():
            d[char] = d.get(char, 0) + 1
    return d

string = "Hello, Python!"
print(alphabet_frequency(string))

#5-2
def alphabet_frequency(s):
    return {char: s.count(char) for char in set(s) if char.isalpha()}

string = "Hello, Python!"
print(alphabet_frequency(string))

#5-3
alphabet_frequency = lambda s: dict([(char, s.count(char)) for char in s if char.isalpha()])

string = "Hello, Python!"
print(alphabet_frequency(string))

#5-4
def alphabet_frequency(s):
  return {char: s.count(char) for char in set(s)}

string = "Hello, Python!"
print(alphabet_frequency(string))