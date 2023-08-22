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