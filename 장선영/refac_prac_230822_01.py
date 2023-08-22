class NumberProcessor:
    def __init__(self, numbers):
        self.numbers = numbers

    def even_numbers(self):
        even_numbers = []
        for i in self.numbers:
            if i % 2 == 0:
                even_numbers.append(i)
        return even_numbers


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_processor = NumberProcessor(numbers)
print(number_processor.even_numbers())
print()

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    number_processor = NumberProcessor(numbers)
    even_numbers_result = number_processor.even_numbers()
    print(even_numbers_result)