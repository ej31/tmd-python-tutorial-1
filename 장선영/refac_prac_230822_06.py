class AlphabetFrequencyCounter:
    def __init__(self, string):
        self.string = string

    def alphabet_frequency(self):
        frequency = {}
        for char in self.string:
            if char.isalpha():
                char_lower = char.lower()
                if char_lower in frequency:
                    frequency[char_lower] += 1
                else:
                    frequency[char_lower] = 1
        return frequency



if __name__ == "__main__":
    string = "Hello, Python"
    frequency_counter = AlphabetFrequencyCounter(string)
    frequency_result = frequency_counter.alphabet_frequency()
    print(frequency_result)