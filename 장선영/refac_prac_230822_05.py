class VowelCounter:
    def __init__(self, string):
        self.string = string

    def count_vowels(self):
        vowels = "aeiouAEIOU"
        count = 0
        for char in self.string:
            if char in vowels:
                count += 1
        return count


string = "Hello, Python"
vowel_counter = VowelCounter(string)
vowel_count = vowel_counter.count_vowels()
print("Number of vowels:", vowel_count)
print()

if __name__ == "__main__":
    string = "Hello, Python"
    vowel_counter = VowelCounter(string)
    vowel_count = vowel_counter.count_vowels()
    print("Number of vowels:", vowel_count)