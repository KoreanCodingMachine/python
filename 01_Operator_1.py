'''
연산자 : 데이터와 대이터를 계산하는 특수문자
수치 연산자 -> 결과값이 숫자로 나오는 경우
논리 연산자 -> 결과값이 true나 false로 나오는 경우

'''
#변수 두개에 각각 숫자 입력
n1 = int(input("숫자 입력 : "))
n2 = int(input("숫자 입력 : "))

'''
        산술 연산자 
            + : 덧셈
            - : 뺄셈
            * : 곱셈
            / : 나눗셈 (소수점 까지)
            % : 나눗셈 (나머지)
            //: 나눗셈 (몫만 나옴)   # 파이썬만 가능
            **: 거듭제곱 (2**3 -> 8) # 파이썬만 가능
            
'''
print(f'{n1}+{n2}= {n1+n2}')
print(f'{n1}-{n2}= {n1-n2}')
print(f'{n1}*{n2}= {n1*n2}')
print(f'{n1}/{n2}= {n1/n2}')
print(f'{n1}%{n2}= {n1%n2}')
print(f'{n1}//{n2}= {n1//n2}')
print(f'{n1}**{n2}= {n1**n2}')



