class NumberAnalyzer:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_max_min(self):
        max_value = max(self.numbers)
        min_value = min(self.numbers)
        return max_value, min_value


numbers = [34, 12, 56, 78, 23]
number_analyzer = NumberAnalyzer(numbers)
max_value, min_value = number_analyzer.find_max_min()
print("Max:", max_value)
print("Min:", min_value)
print()

