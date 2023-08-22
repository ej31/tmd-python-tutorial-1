

class CntVow:

    def __init__(self):
        self.count_vowels

    def count_vowels(self, in_str):
        vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        count_num = 0
        for i in in_str:
            if i in vowel_list:
                count_num += 1
        return count_num