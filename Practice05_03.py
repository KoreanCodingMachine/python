num1 = int(input("정수 1 입력 >>>"))
num2 = int(input("정수 2 입력 >>>"))
num3 = int(input("정수 3 입력 >>>"))

if(num1 >= num2 and num1 >= num3):    #num1이 가장 클때
    print(f"가장 큰수는{num1}입니다.")
elif(num1 <= num2 and num2 >= num3):
    print(f"가장 큰 수는{num2}입니다.")  #num2가 가장 클때
else:
    print(f"가장 큰 수는{num3}입니다.")  #num3가 가장 클때



