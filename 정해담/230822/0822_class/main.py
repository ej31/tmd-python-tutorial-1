from class_alphabet import AlphabetCount
from class_cnt_vowels import CntVow
from class_even_numbers import EveNum
from class_find_max_min import MaxMin
from class_reverse_string import ReverseStr
from class_sum_elements import SumElements

input_str = "Hello Python World!😎"
input_int_list = [27, 8, 31, 97, 81, 13]


if __name__ == '__main__':
    alpha = AlphabetCount().alphabet_frequency(input_str)
    cntvow = CntVow().count_vowels(input_str)
    evenum = EveNum().even_numbers(input_int_list)
    maxmin = MaxMin().find_max_min(input_int_list)
    revstr = ReverseStr().reverse_string(input_str)
    sumele = SumElements().sum_elements(input_int_list)

    print(alpha)
    print(cntvow)
    print(evenum)
    print(maxmin)
    print(revstr)
    print(sumele)