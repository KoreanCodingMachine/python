'''
map(function, iterable)

map 함수의 모양은 위와 같습니다.
첫 번째 매개변수로는 함수가 오고
두 번째 매개변수로는 반복 가능한 자료형(리스트, 튜플 등)이 옵니다.

map 함수의 반환 값은 map객체 이기 때문에 해당 자료형을 list 혹은 tuple로 형 변환시켜주어야 합니다.

함수의 동작은 두 번째 인자로 들어온 반복 가능한 자료형 (리스트나 튜플)을
첫 번째 인자로 들어온 함수에 하나씩 집어넣어서 함수를 수행하는 함수입니다.

map(적용시킬 함수, 적용할 값들) 이런 식인 거죠.
예를 들어 첫 번째 인자가 값에 +1을 더해주는 함수라고 하고 두번째 인자에 [1, 2, 3, 4, 5] 라는 리스트를 집어넣으면

함수의 모양은 아래와 같고
map( 값에 +1 을 더해주는 함수, [1,2,3,4,5])
함수의 반환을 list(. )로 감싸주면
[2,3,4,5,6] 이 되는 함수입니다.

https://blockdmask.tistory.com/531
'''
# 리스트에 값을 하나씩 더해서 새로운 리스트를 만드는 작업
myList = [1, 2, 3, 4, 5]
# for 반복문 이용
result1 = []
for val in myList: result1.append(val + 1)
print(f'result1 : {result1}')
# # map 함수 이용
def add_one(n): return n + 1
result2 = list(map(add_one, myList))
# map반환을 list 로 변환
print(f'result2 : {result2}')
