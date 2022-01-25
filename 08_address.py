#메모리 주소 안바뀌는 형태
#mutable --> list,set,dict
#프로그램과 프로세스 , 실행할때마다 저장되는 주소가 다르다.
#추가,삭제한다고 메모리 주소가 바뀌지 않는다.
lst =[1,2,3,4,5]
print(id(lst))
lst.append(6)
print(id(lst))
lst.pop(3)
print(id(lst))
s = {1,2,3,4,5}
print(id(s))
s.pop()
print(id(s))
s.add(100)
print(id(s))

#메모리 주소가 바뀌는 형태
#immutable --> int, float, str, tuple
#값을 넣은 공간이 따로 저장되어있다.
num = 10
print(num,id(num))
num = 20
print(num,id(num))
num = 10
print(num,id(num))
num += 20
print(num,id(num))
newNum = num #동일한 메모리 주소를 저장 num의 저장된 위치를 newNum에 저장한다.
print(id(num),id(newNum))