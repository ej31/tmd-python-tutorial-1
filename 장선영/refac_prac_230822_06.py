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



