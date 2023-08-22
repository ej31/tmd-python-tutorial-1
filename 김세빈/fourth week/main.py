from class_merge import StringUtilFunc

if __name__ == '__main__':
    _util_ogj = StringUtilFunc
    string = "Hello, Python!"
    string_kor = "파이썬"

print(StringUtilFunc().alphabet_frequency(string))
print(StringUtilFunc().count_vowels(string))
print(StringUtilFunc().reverse_string(string_kor))

'''
1.
class 자체를 파일 내에서 사용할 때에는 사용시 클래스명.함수명 사용이 가능하지만,
다른 파일에 있는 클래스를 불러오고 싶을 경우에는 클래스명().함수명으로 사용해야한다

2.
클래스 사용시 이름은 _가 아닌 대문자로 구별할 수 있도록!

3. 
crtl 누른 채로 마우스로 클릭하면 해당 함수가 참조하고 있는 곳을 확인할 수 있음

4. 
import sys
의 형태는 파이썬 2에서 사용하던 구식 형태(완전 다른 파일에 있는 함수를 모듈을 선언하여 가져오는 방식)
지금은 사용하지 말자!

5. 
class에서 def를 선언할 경우, 해당 함수에서 self 인자를 쓰지 않으려면 @staticmethod을 사용해야함

6.
__init__ 에서 정의되는 인수를 사용하지 않을 경우엔 그냥 인수를 지우고 가야함
'''