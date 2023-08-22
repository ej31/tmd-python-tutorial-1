class String_Utility:
    def __init__(self, string):
        self.__string = string

    def reverse_string(self):
        rever_str = self.__string[::-1]
        return rever_str

    def count_vowels(self):
        vowels = ["a", "e", "i", "o", "u", "y"]
        value = 0
        for i in self.__string:
            if i in vowels:
                value += 1
        return value

    def alphabet_frequency(self):
        final_dict = {}
        alpha_num = 0
        for i in self.__string:
            if i.isalpha():
                alpha_num = self.__string.count(i)
                final_dict[i] = alpha_num
        return final_dict

example1 = String_Utility("every step I take, every move I make")
print(example1.alphabet_frequency())
print(example1.reverse_string())
print(example1.count_vowels())
