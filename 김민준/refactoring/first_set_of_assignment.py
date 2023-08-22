class FirstSetOfAssignment:

    def __init__(self, num):
        self._num = num

    def print_even_numbers(self):
        for i in range(1, self._num):
            if i % 2 == 0:
                print(f"{i}")
            elif i % 2 != 0:
                continue

    def print_even_numbers_with_for_loop(self):
        for i in range(2, self._num, 2):
            print(i)

    def time_table(self):
        for _i in range(1, self._num - 1):
            for _j in range(1, self._num - 1):
                print(f"{_i * _j}", end = "\t")
            print()

    def right_triangle(self):
        for _i in reversed(range(1, self._num)):
            for _j in range(_i, self._num):
                print("*", end = "")
        print()

    def upside_down_triangle(self):
        for _i in range(1, self._num):
            for _j in reversed(range(_i, self._num)):
                print("*", end = "")
            print()

    def equilateral_triangle(self):
        for i in range(self._num):
            for n in range(self._num - i + 1):
                print(" ", end = "")
            for m in range(2 * i + 1):
                print("*", end = "")
            print()

    def upside_down_equilateral_triangle(self):
        for i in range(self._num, 0, -1):
            for n in range(self._num - i):
                print(" ", end = "")
            for m in range(2 * i - 1):
                print("*", end = "")
            print()