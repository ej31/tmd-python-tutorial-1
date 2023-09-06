# List(int) 에 관한 함수들

class AllNumberFunctions:
    def __init__(self, numbers):
        self.__numbers = numbers

    def even_numbers(self):
        """
        짝수만 반환하는 함수
        """
        _tmp = self.__numbers.copy()
        for number in _tmp:
            if number % 2 == 0:
                continue
            elif number % 2 == 1:
                _tmp.remove(number)
        return _tmp

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
