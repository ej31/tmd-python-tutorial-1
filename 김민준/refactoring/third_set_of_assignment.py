class ThirdSetOfAssignment:

    def __init__(self, num, string, num_list, char_list):
        self._num = num
        self._string = string
        self._num_list = num_list
        self._char_list = char_list

    def even_numbers(self):
        even_list = []

        for i in self._num_list:
            if i % 2 == 0:
                even_list.append(i)

        return print(even_list)

    def reverse_string(self):
        return self._string[::-1]

    def sum_elements(self):
        total = 0

        for i in self._num_list:
            total += i

        return total

    def find_min_max(self):
        _max = 0
        _min = 0

        for i in self._num_list:
            if i > _max:
                _max = i
            elif i < _max:
                continue

        for j in self._num_list:
            if j < _min:
                _min = j
            elif _min == 0:
                _min = j

        return _max, _min

    def count_vowels(self):
        vowels = "AEIOUWYaeiouwy"
        vowel_count = 0

        for i in self._string:
            if i in vowels:
                vowel_count += 1

        return vowel_count

    def alphabet_frequency(self):
        alpha_freq = {}
        only_alphabet = []

        for i in self._string:
            if i.isalpha():
                only_alphabet.append(i)
            elif not i.isalpha():
                continue

        for i in only_alphabet:
            if i in alpha_freq:
                alpha_freq[i] += 1
            else:
                alpha_freq[i] = 1

        return str(alpha_freq)