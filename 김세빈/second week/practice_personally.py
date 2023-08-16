#리스트 요소 합계 구하기
sum_list = [1,2,3,4,5,6,7,8,9,10]
_sum = 0
for num in sum_list:
    _sum += num
print(_sum)


#홀짝 분류(1~50)
deter_list = list(range(1,51))
even_list = []
odd_list = []
for i in deter_list:
    if i % 2 == 0:
        even_list.append(i)
    elif i % 2 != 0:
        odd_list.append(i)

print(f"짝수 리스트는: {even_list}\n홀수 리스트는: {odd_list}")


#최댓값 찾기(파이썬 내장함수 x)
number_list = [46,13,74,52,7,25,68,41]
max_num = number_list[0]
for i in number_list:
    if i > max_num:
        max_num = i
print(f"최댓값은 {max_num}")


#소수 판별(1과 자기자신만을 약수로 가지는 수)
prime_num = int(input("임의의 숫자를 입력하여 주세요: "))
measure = []
for j in range(1,prime_num+1):
    if prime_num % j == 0:
        measure.append(j)
print(f"약수는: {measure}")

if len(measure) == 2:
    print("소수 입니다!")
else:
    print("소수가 아닙니다.")


#리스트 요소 위치 교환
change_list = [1,2,3,4,5,6,7,8]
first_change = int(input("위치를 변경하고 싶은 첫번째 수의 위치를 입력: ")) -1
sec_change = int(input("위치를 변경하고 싶은 두번째 수의 위치:")) -1

temp = 0
temp = change_list[first_change]
change_list[first_change] = change_list[sec_change]
change_list[sec_change] = temp
print(change_list)


#리스트에서 한 칸 씩 회전시키기
num_list = [1,2,3,4,5,6,7,8,9,10]
copy_num_list = num_list.copy()

length = len(copy_num_list)
_temp = copy_num_list[0]

for i in range(0, length):
    if i < length - 1:
        copy_num_list[i] = copy_num_list[i+1]
        copy_num_list[length-1] = _temp

print(num_list)
print(copy_num_list)

#리스트 합집합과 교집합
list_one = [1,2,3,4,5,6,7,8]
list_two = [5,6,7,8,9,10]

two_list = list_one +list_two
sum_list = []

for num in two_list:
    if num not in sum_list:
        sum_list.append(num)
print(f"합집합은 {sorted(sum_list)}")

intersection = list(set(list_one) & set(list_two))
print(f"교집합은 {sorted(intersection)}")


#리스트 평균과 분산
cal_list = [1,2,3,4,5,6,7,8,9,10]

mean = sum(cal_list) / len(cal_list)
print(mean)

var = 0
for val in cal_list:
    var = var + (val - mean)**2
    variance = var / len(cal_list)
print(variance)