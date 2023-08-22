# 6번문제 -------------------------------------------------------------------------------------------

def alphabet_frequency(s):
    final_dict = {}
    alpha_num = 0
    for i in s:
        if i.isalpha() == True:
            alpha_num = s.count(i)
            final_dict[i] = alpha_num

    return final_dict

string = "Hello, Python!"

print(alphabet_frequency(string))