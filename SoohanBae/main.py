from collections import defaultdict
from string import punctuation, whitespace

# list(int)에 관한 함수들


class AllNumberFuncitons:
    def __init__(self, numbers):
        self.__numbers = numbers

    def even_numbers(self):
        """
        짝수만 반환하는 함수
        """
        tmp = self.__numbers.copy()
        for number in tmp:
            if number % 2 == 0:
                continue
            elif number % 2 == 1:
                tmp.remove(number)
        return tmp

    def sum_elements(self):
        """
        값의 합을 반환하는 함수
        """
        return sum(self.__numbers)

    def find_max_min(self):
        """
        값의 최대최소를 tuple로 반환하는 함수
        """
        return (max(self.__numbers), min(self.__numbers))

# 문자열에 관한 함수들


class AllStringFunctions:
    def __init__(self, string):
        self.__string = string

    def reverse_string(self):
        """
        string을 뒤집어 반환하는 함수
        """
        return self.__string[::-1]

    def count_vowels(self):
        """
        모음의 개수만 반환하는 함수
        """
        ans = 0
        for w in self.__string:
            if w.lower() in 'aeiou':
                ans += 1
        return ans

    def alphabet_frequency(self):
        """
        문자열을 입력받아 빈도를 사전 형태로 반환하는 함수
        """
        tmp_dict = defaultdict(int)
        for w in self.__string:
            if w not in punctuation and w not in whitespace:
                tmp_dict[w] += 1
        return tmp_dict


# 클래스 정의 (자동차 틀)
class Car:
    def __init__(self, color, model):
        self._color = color
        self._model = model
        self._is_running = False

    def start_engine(self):
        if not self._is_running:
            print(f"{self._color} 색상 {self._model} 모델 자동차의 엔진이 시작되었습니다.")
            self._is_running = True
        else:
            print("이미 엔진이 작동 중입니다.")

    def accelerate(self):
        if self._is_running:
            print(f"{self._color} 색상 {self._model} 모델 자동차가 가속 중입니다.")
        else:
            print("먼저 엔진을 시작하세요.")

    def stop(self):
        if self._is_running:
            print(f"{self._color} 색상 {self._model} 모델 자동차가 정지되었습니다.")
            self._is_running = False
        else:
            print("이미 엔진이 꺼져 있습니다.")


# 실제 작동하는 함수


def main():
    # 객체 생성
    red_car = Car(color="빨간", model="세단")
    blue_car = Car(color="파란", model="SUV")

    # 객체의 메서드 호출 (자동차 작업)
    red_car.start_engine()
    red_car.accelerate()
    red_car.stop()

    blue_car.start_engine()
    blue_car.accelerate()

    num_obj = AllNumberFuncitons(numbers=[1, 2, 3, 4, 5])
    str_obj = AllStringFunctions("Hello Python!")

    print("숫자형 리스트에 대해 짝수만 반환한 결과: ", num_obj.even_numbers())
    print("숫자형 리스트에 대해 합을 반환한 결과: ", num_obj.sum_elements())
    print("숫자형 리스트에 대해 최대 최소 값을 반환한 결과: ", num_obj.find_max_min())
    print("문자열을 뒤집은 결과: ", str_obj.reverse_string())
    print("문자열에 대해 모음만 반환한 결과: ", str_obj.count_vowels())
    print("문자열에 대해 알파벳 빈도를 계산한 결과: ", str_obj.alphabet_frequency())


if __name__ == '__main__':
    main()
