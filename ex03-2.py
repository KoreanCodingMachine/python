list_month = [31,28,31,30,31,30,31,30,31,30,31,30]
month = int(input("1~12 사이의 월을 입력하세요 >>> "))

print('{}월은 {}일까지 있습니다.'.format(month,list_month[month-1]))