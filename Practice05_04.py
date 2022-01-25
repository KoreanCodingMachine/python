car_num = input("차량번호를 입력하세요 >>>")
number = car_num[-4]+car_num[-3]+car_num[-2]+car_num[-1]
#print(number)
real_car_num = int(number)
if(real_car_num % 2 == 0):
    print(f"차량번호 '{car_num}'는 오늘 운행가능입니다.")
else:
    print(f"차량번호 '{car_num}'는 오늘 운행불가능입니다.")
