'''

    데이터 타입(35p)
        1.정수형 : int
        2.문자열 : str
        3.실수형 : float
        4.논리형 : bool

데이터 형변환 ---> 데이터 타입을 다른 데이터 타입으로 변경
1.정수로 형변환
    -int(1.9) --> 1   (소수점 숫자를 제거)
    -int('200') --> 200 (문자열을 숫자로 변환)
    -int('3.1415') --> 에러 발생(문자열이 정수가 아니라 실수)
    -int(True) --> 1
    -int(False) --> 0
'''
print(int(1.9))
print(int(-1.9))
print(int('200'))
#print(int('3.1415'))
print(int(True))
print(int(False))
'''
2. 실수로 형변환
    -float(20) --> 20.0 
    -float('3.14145') --> 3.1415
    -float('20') --> 20.0  
    -float(False) --> 0.0
    -float(True)) --> 1.0
    ctrl + d -> 복사
    shift + delete -> 한줄 씩 삭제
    ctrl + shift --> 코드 위아래 순서 변경 
 
'''
print(float(20))
print(float('20'))
print(float("3.1415"))
print(float(False))
print(float(True))

'''
3.문자열 형변환
    - str(값)
'''
print(type(str(111)))
print(str(3.1415))
print(str(True))
'''
4.논리값으로 형변환
    -bool(0) -->  False   // 0 이외의 모든 숫자는 True
    -bool(0이 아닌 숫자) --> True
    -bool('Hello') --> True
    -bool('') --> False 
'''
print(bool(0))
print(bool(1))
print(bool(-1))
print(bool('Hello'))
print(bool(''))
