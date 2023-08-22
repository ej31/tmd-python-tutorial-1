
from refac_prac_230822_01 import NumberProcessor
from refac_prac_230822_02 import StringReverser
from refac_prac_230822_03 import NumberSummer
from refac_prac_230822_04 import NumberAnalyzer
from refac_prac_230822_05 import VowelCounter
from refac_prac_230822_06 import AlphabetFrequencyCounter


#01
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    number_processor = NumberProcessor(numbers)
    even_numbers_result = number_processor.even_numbers()
    print(even_numbers_result)

numbers = [11, 22, 33, 44, 55]
number_processor = NumberProcessor(numbers)
even_numbers_result = number_processor.even_numbers()
print(even_numbers_result)
print("---------------------")

#02
if __name__ == "__main__":
    example_string = "파이썬"
    string_reverser = StringReverser(example_string)
    reversed_string = string_reverser.reverse_string()
    print(reversed_string)

input_string = "Hello, World"
string_reverser = StringReverser(input_string)
reversed_string = string_reverser.reverse_string()
print(reversed_string)
print("---------------------")


#03
if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50]
    number_summer = NumberSummer(numbers)
    sum_result = number_summer.sum_elements()
    print(sum_result)

numbers = [15, 25, 35, 45, 55]
number_summer = NumberSummer(numbers)
sum_result = number_summer.sum_elements()
print(sum_result)



#04
if __name__ == "__main__":
    numbers = [34, 12, 56, 78, 23]
    number_analyzer = NumberAnalyzer(numbers)
    max_value, min_value = number_analyzer.find_max_min()
    print("Max:", max_value)
    print("Min:", min_value)

numbers = [45, 67, 12, 89, 34]
number_analyzer = NumberAnalyzer(numbers)
max_value, min_value = number_analyzer.find_max_min()
print("Max:", max_value)
print("Min:", min_value)
print("---------------------")

# 05
if __name__ == "__main__":
    string = "Hello, Python"
    vowel_counter = VowelCounter(string)
    vowel_count = vowel_counter.count_vowels()
    print("Number of vowels:", vowel_count)

string = "Hello, World"
vowel_counter = VowelCounter(string)
vowel_count = vowel_counter.count_vowels()
print("Number of vowels:", vowel_count)
print("---------------------")

# 06
if __name__ == "__main__":
    string = "Hello, Python"
    frequency_counter = AlphabetFrequencyCounter(string)
    frequency_result = frequency_counter.alphabet_frequency()
    print(frequency_result)
    
string = "Hello, World"
frequency_counter = AlphabetFrequencyCounter(string)
frequency_result = frequency_counter.alphabet_frequency()
print(frequency_result)
print("---------------------")


