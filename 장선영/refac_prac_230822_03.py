class NumberSummer:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum_elements(self):
        total_sum = 0
        for num in self.numbers:
            total_sum += num
        return total_sum


numbers = [10, 20, 30, 40, 50]
number_summer = NumberSummer(numbers)
sum_result = number_summer.sum_elements()
print(sum_result)


if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50]
    number_summer = NumberSummer(numbers)
    sum_result = number_summer.sum_elements()
    print(sum_result)