class string_util_func:
    def __init__(self, s: str):
        self.__string_util = string_util
        pass

    def alphabet_frequency(string_util):
        """
        문자열을 입력받아 각 알파벳 문자의 빈도를 사전 형태로 반환
        :return:
        """
        frec_dict = {}
        for alpha in string_util:
            if alpha.isalpha():
                if alpha in frec_dict:
                    frec_dict[alpha] += 1
                else:
                    frec_dict[alpha] = 1
        return frec_dict

    def count_vowels(string_util):
        """
        문자열을 입력받아 그 중 영어 모음의 개수를 반환하는 함수
        :return:
        """
        vowel_num = 0
        vowel_list = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        for i in string_util:
            if i in vowel_list:
                vowel_num += 1
        return vowel_num

    def reverse_string(string_util):
        """
        문자열을 입력받아 그 문자열을 거꾸로 뒤집은 결과를 반환하는 함수
        :return:
        """
        return string_util[::-1]

string = "Hello, Python!"
string_kor = "파이썬"
print(string_util_func.alphabet_frequency(string))
print(string_util_func.count_vowels(string))
print(string_util_func.reverse_string(string_kor))