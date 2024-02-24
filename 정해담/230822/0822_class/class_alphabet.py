

class AlphabetCount:
    def __init__(self):
        self.alphabet_frequency

    def alphabet_frequency(self, __s):

        char_count = {}
        for char in __s:
            if char.isalpha():
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
        return char_count

