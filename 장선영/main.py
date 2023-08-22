#01
from refac_prac_230822_01 import NumberProcessor

numbers = [11, 22, 33, 44, 55]
number_processor = NumberProcessor(numbers)
even_numbers_result = number_processor.even_numbers()
print(even_numbers_result)
print("---------------------")

#02
from refac_prac_230822_02 import StringReverser

input_string = "Hello, World"
string_reverser = StringReverser(input_string)
reversed_string = string_reverser.reverse_string()
print(reversed_string)
print("---------------------")


#03
from refac_prac_230822_03 import NumberSummer

numbers = [15, 25, 35, 45, 55]
number_summer = NumberSummer(numbers)
sum_result = number_summer.sum_elements()
print(sum_result)



#04
from refac_prac_230822_04 import NumberAnalyzer

numbers = [45, 67, 12, 89, 34]
number_analyzer = NumberAnalyzer(numbers)
max_value, min_value = number_analyzer.find_max_min()
print("Max:", max_value)
print("Min:", min_value)
print("---------------------")
# 05
from refac_prac_230822_05 import VowelCounter

string = "Hello, World"
vowel_counter = VowelCounter(string)
vowel_count = vowel_counter.count_vowels()
print("Number of vowels:", vowel_count)
print("---------------------")
# 06
from refac_prac_230822_06 import AlphabetFrequencyCounter
string = "Hello, World"
frequency_counter = AlphabetFrequencyCounter(string)
frequency_result = frequency_counter.alphabet_frequency()
print(frequency_result)
print("---------------------")


