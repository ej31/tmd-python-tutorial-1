class SecondSetOfAssignment:

    def __init__(self, num, num_list, char_list):
        self._num = num
        self._num_list = num_list
        self._char_list = char_list

    def extract_odd_number(self):
        odd_numbers: list[int] = []

        for i in self._num_list:
            if i % 2 == 0:
                continue
            elif i % 2 != 0:
                odd_numbers.append(i)

        print(odd_numbers)

    def find_min_max(self):
        max_value = self._num_list[0]
        min_value = self._num_list[0]

        for _i in self._num_list:
            if _i > max_value:
                max_value = _i
            elif _i < min_value:
                min_value = _i

        print(f"Maximum value: {max_value}")
        print(f"Minimum value: {min_value}")

    def remove_dup_in_list(self):
        unique_fruits = []

        for item in self._char_list:
            if item not in unique_fruits:
                unique_fruits.append(item)

        print(f"Original fruits list: {self._char_list}")
        print(f"List with duplicated removed: {unique_fruits}")

    def separate_odd_and_even(self):
        even_numbers = []
        odd_numbers = []

        for i in self._num_list:
            if i % 2 == 0:
                even_numbers.append(i)
            elif i % 2 != 0:
                odd_numbers.append(i)

        print(f"Even numbers: {even_numbers}")
        print(f"Odd numbers: {odd_numbers}")

    def multiply_elements_from_list(self):
        result = 1

        for i in self._num_list:
            result *= i

        print(f"Result of Multiplication: {result}")

    def create_new_list_by_merge(self):
        zipped_list = zip(self._char_list, self._num_list)  # combining to two list with zip() to set a iterator

        combined_list = list(zipped_list)  # using list() to convert a iterator to list

        return print(combined_list)
