class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_string(self):
        reversed_string = self.input_string[::-1]
        return reversed_string


example_string = "파이썬"
string_reverser = StringReverser(example_string)
reversed_string = string_reverser.reverse_string()
print(reversed_string)
print()

if __name__ == "__main__":
    example_string = "파이썬"
    string_reverser = StringReverser(example_string)
    reversed_string = string_reverser.reverse_string()
    print(reversed_string)