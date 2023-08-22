import drawing_pentagram
from first_set_of_assignment import FirstSetOfAssignment
from second_set_of_assignment import SecondSetOfAssignment
from third_set_of_assignment import ThirdSetOfAssignment
from drawing_pentagram import PentagramDrawing

if __name__ == '__main__':
    num = 11
    char_list = ["apple", "kiwi", "banana", "strawberry", "melon"]
    num_list = [5, 7, 2, 10, 2, 1]
    string = "Hello, World!"

    first_asgnmt_ex1 = FirstSetOfAssignment(num)
    second_asgnmt_ex1 = SecondSetOfAssignment(num, num_list, char_list)
    third_asgnmt_ex1 = ThirdSetOfAssignment(num, string, num_list, char_list)

    first_asgnmt_ex1.equilateral_triangle()
    second_asgnmt_ex1.create_new_list_by_merge()
    print(third_asgnmt_ex1.count_vowels())

    PentagramDrawing()
