'''
    논리연산자
        and  : 양쪽의 조건이 둘다 true가 되는 연산자
        or   : 양쪽의 조건식 중 하나라도 true가 되면 true가 되는 연산자
        not  : 오른쪽에 있는 조건식의 결과를 반대로 뒤집는 연산
               true -> false , false -> true 로 뒤집는 연산
'''

n1,n2 = 10,7
print(n1 > 5 and n2 < 7) #False
print(n1 > 5 and n2 < 10) #True
print(n1 > 5 or  n2 < 7) #True
print(n1 < 5 or  n2 < 7) #False

result = n1 > 10
print(not result) # not False -> True
#n1 > 5 n2< 10 n1과 n2가 다른가?
result = n1>5 and n2<10 and n1!=n2 # True
print(result)
