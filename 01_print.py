# 이스케이프 : 특수문자 표현 방식, \ 역슬래쉬로 시작되는 문자열
#줄바꿈 문자 : \n
print('H\ne\nl\nl\no')

#탭 \t
print("번호\t이름\t\t번호")
print("1\t김철수\t1234")
print("2\t이훈\t\t1234")

# " , ' 출력   --> \" , \'
print("오늘은 \"파이썬\" 수업이 있는날입니다.") # c,c++,java
print('오늘은 "파이썬" 수업이 있는 날입니다.') # python만 가능
print("오늘은 '파이썬' 수업이 있는 날입니다.") # python만 가능

#키워드 속성
#1. sep : 출력할 데이터들 사이에 어떤 문자를 넣을것인지
#         생략시 기본값으로 공백이 들어감
print(2022,1,18) # ,사용시 출력할 데이터 사이에 공백
print(2022,1,18,sep = '-')
print(2022,1,18,sep = '/')
#2. end: 출력후 어떤 문자열을 넣을것인가
#        생략시 줄바꿈이 들어감
print('김철수',end=',') #줄바꿈 대신 , 
print('김철수')
