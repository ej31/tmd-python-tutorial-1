from menu import *
from soup import *
from side_dish import *

introduction_menu = """랜덤한 저녁 메뉴 고르기(반찬, 국 중 하나만) : 1
랜덤한 저녁 메뉴 고르기(반찬, 국 둘 다) : 2
반찬/국 중 하나 고르기 : 3 / 4
저녁 메뉴 전체 레시피 보기 : 5
종료하기 : 6\n"""
return_menu = "반찬 복불복으로 >> 1  반찬, 국 복불복으로 >> 2   반찬 / 국 고르기 >> 3 / 4    메뉴로 >> 5    종료 >> 6\n"
failed_menu = "팔지 않는 메뉴입니다. 다시 입력해 주세요!\n"
menu_diction_1 = {1: print_gal,
                  3: print_gogalby,
                  5: print_cucumber_muchim,
                  7: print_pork_neck,
                  9: print_lettuce_kimchi,
                  11: print_braised_tofu,
                  13: print_braised_radish_with_mackerel}
menu_diction_2 = {2: print_JJagle,
                  4: print_Perilla_Kimchi,
                  6: print_Seaweed_Soup,
                  8: print_Beef_Bone_Soup,
                  10: print_Soybean_Sprout_Soup}

menu_diction_1.update(menu_diction_2)
# print(menu_diction_1)
print(introduction_menu)
#class / try / exception / raise 찾아보기

# 무한 반복
while True:
    try:
        dinner = int(input(""))
        # 랜덤한 숫자 뽑아내기
        import random

        random_number_1 = random.randint(1, 9)
        random_number_2 = random.randint(1, 9)
        # 1 입력시 랜덤한 숫자 출력 후 문장 출력 및 26번줄로 돌아감
        if dinner == 1:
            print(f"{random_number_1}\n{return_menu}")
        # 2 입력시 랜덤한 숫자 두개 출력 후 문장 출력 및 26번줄로 돌아감
        elif dinner == 2:
            print(f"( {random_number_1} / {random_number_2} )\n{return_menu}")
        # 3 입력시 메뉴판 출력
        elif dinner == 3:
            print_side_dish()
            food = int(input("원하시는 반찬의 번호를 선택해주세요\n"))
            if food == 0:
                print(introduction_menu)
            elif food in menu_diction_1:
                menu_diction_1[food]()
                print(return_menu)
            else:
                print(failed_menu)
        elif dinner == 4:
            print_soup()
            food = int(input("원하시는 국의 번호를 선택해주세요\n"))
            if food == 0:
                print(introduction_menu)
            elif food in menu_diction_2:
                menu_diction_2[food]()
                print(return_menu)
            else:
                print(f"{failed_menu}\n")
        elif dinner == 5:
            print_menu()
            food = int(input("\n메뉴의 번호를 입력하세요!\n"))
            # 0 입력시 introduction_menu 호출 후 26번줄로 돌아감
            if food == 0:
                print(introduction_menu)
            # 1 입력 후 숫자에 해당하는 레시피 출력 후 26번줄로 돌아감
            elif food in menu_diction:
                menu_diction[food]()
                print(return_menu)
            # 메뉴판 이외의 숫자 입력 시 문장 출력 후 26번줄로 돌아감
            else:
                print(f"{failed_menu}\n")
        # 코드 종료
        else:
            print("장비를 정지합니다.")
            # 코드 이탈
            break
    except InvalidMenuException as e:
        print("잘못된 메뉴!")
