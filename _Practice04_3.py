employee_num = int(input("4자리 사원번호를 입력하세요 >>>"))
employee_hour = employee_num % 10
if employee_hour>=5:
    print("근무 시간은 오전입니다.")
else:
    print("근무 시간은 오후입니다.")

'''
employee_no = int(input("4자리 사원번호를 입력하세요>>>"))
#employee_no %=10 
msg = '오전' if employee_no %10 >=5 else '오후'
print("근무 시간은 {msg}입니다.")    
'''