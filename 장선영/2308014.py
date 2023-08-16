empty_tuple = ()
tuple_type_1 = (100,)
tuple_type_2 = (1, 2, 3, 4, "Hello", "this is text")

print(tuple_type_2[0])
print(tuple_type_2[1])
print(tuple_type_2[2])
print(tuple_type_2[5])

# 튜플의 길이 확인
tuple_type_2 = (1, 2, 3, 4, "Hello", "this is text")
type_2_length = len(tuple_type_2)
print(type_2_length)
# 길이는 언제나 인덱스 +1
# off by one  inssue

# 튜플 slice
fruits_tuple = ('apple', 'banana', 'orange', 'grape', 'melon')

# 0부터 2번 인덱스까지 출력
after_slice_type_1 = fruits_tuple[0:3]
print(f"{after_slice_type_1} == {fruits_tuple[0:3]}")

after_slice_type_2 = fruits_tuple[::-1]
print(f"{after_slice_type_2} == {fruits_tuple[::-1]}")

after_slice_type_3 = fruits_tuple[2:]
print(f"{after_slice_type_3} == {fruits_tuple[2:]}")

after_slice_type_4 = fruits_tuple[:4]
print(f"{after_slice_type_4} == {fruits_tuple[:4]}")

# 튜플과 zip함수

fruits = ('apple', 'banana', 'orange')
prices = (1.2, 0.9, 1.5)
quantities = (3, 5, 2)

zip_fruits_info = zip(fruits, prices, quantities)

# index(), count()

fruits = ('apple', 'banana', 'orange', 'cherry', 'melon')
# index()  안 쪽에 값이 몇 번 인덱스인지 찾음
print(fruits.index('orange'))
# count()  안 쪽에 값이 몇 번 등장하는지 알려준다.  없으면 0
print(fruits.count('orange'))

# 빈 딕셔너리 선언 (생성)
empty_dict = {}

# 일반적인 형태의 딕셔너리
dict_type_1 = {"apple": 1.4, "cherry": 1.5}
print(dict_type_1)

# 딕셔너리 업데이트
fruit_cost_dict_1 = {"apple": 100, "cherry": 50}
fruit_cost_dict_2 = {"apple": 5, "melon": 100}

fruit_cost_dict_1.update(fruit_cost_dict_2)

print(fruit_cost_dict_2)

# 업데이트 대안책으로 in절을 사용한다.
if "apple" in fruit_cost_dict_1:
    fruit_cost_dict_1["apple"] = 5000

if "grape" not in fruit_cost_dict_1:
    fruit_cost_dict_1["grape"] = 100

print(fruit_cost_dict_1)

empty_set = {}

set_fruit_type_2 = {"apple", "apple", "apple"}
print(set_fruit_type_2)

# set 요소 추가 및 갱신
set_fruit = {"apple", "banana", "mango", "cherry"}
print(f"set_fruit before add -- {set_fruit}")
set_fruit.add("melon")
print(f"set_fruit after add -- {set_fruit}")

set_fruit.update(("strawberry", "blueberry"))
print(f"set_fruit after update -- {set_fruit}")

# set 요소 삭제
set_fruit_type_2 = {"apple", "banana", "mango"}
set_fruit_type_2.remove("apple")
print(f"set_fruit_type_2 after remove --{set_fruit_type_2}")

set_fruit_type_2.discard("mango")
print(f"set_fruit_type_2 after remove -- {set_fruit_type_2}")





def some_method()
    print()
