from car_module import Car
from allnumberfunctions_module import AllNumberFunctions
from allstringfunctions_module import AllStringFunctions


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

    num_obj = AllNumberFunctions(numbers=[1, 2, 3, 4, 5])
    str_obj = AllStringFunctions("Hello Python!")

    print("숫자형 리스트에 대해 짝수만 반환한 결과: ", num_obj.even_numbers())
    print("숫자형 리스트에 대해 합을 반환한 결과: ", num_obj.sum_elements())
    print("숫자형 리스트에 대해 최대 최소 값을 반환한 결과: ", num_obj.find_max_min())
    print("문자열을 뒤집은 결과: ", str_obj.reverse_string())
    print("문자열에 대해 모음만 반환한 결과: ", str_obj.count_vowels())
    print("문자열에 대해 알파벳 빈도를 계산한 결과: ", str_obj.alphabet_frequency())


if __name__ == '__main__':
    main()
