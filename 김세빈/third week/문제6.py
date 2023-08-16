#문자열을 입력받아 각 알파벳 문자의 빈도를 사전 형태로 반환
def alphabet_frequency(s):
    frec_dict = {}
    for alpha in s:
        if alpha.isalpha():
            if alpha in frec_dict:
                frec_dict[alpha] += 1
            else:
                frec_dict[alpha] = 1
    return frec_dict

string = "Hello, Python!"
print(alphabet_frequency(string))