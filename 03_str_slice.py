'''
    문자열 슬라이스
    형식
    문자열[begin;end;step;]
        1)begin : 시작 인덱스, 포함, 생략하면 0부터 시작
        2)end : 종료 인덱스,불포함, 생략하면 인덱스번호 끝까지
        3)step: 증가/감소, 생략하면 1씩 증가
'''

s = 'Hello World'
print(s[0:6]) #0번 인덱스 ~ 5번 인덱스까지 , 띄어쓰기까지 출력(drag해서 확인)
print(s[::]) #전부 출력
print(s[0:8:2]) #0번 인덱스 7번 인덱스까지 인덱스 번호를 2씩 증가
print(s[:9]) # 0번 인덱스 ~ 8번 인덱스까지 
print(s[-4:])
print(s[-9:-4]) # 앞에 작은 숫자가 나와야 한다. 서로 바뀌면 아무것도 출력x

#내장함수 - len(문자열)
#len('Hello') --> 5   글자수 구해주는 함수
print(len(s)) #11

tel1 = '02-543-1234'
tel2 = '010-1234-5678'

#tel1과 tel2의 뒷번호 4자리만 추출해서 출력
print(tel1[-4:])
print(tel2[-4:])

#tel1과 tel2의 뒷자리 4자리만 제외하고 추출해서 출력
print(tel1[:-4])
print(tel2[:-4])

#마이너스 인덱스를 사용하지 않고 추출
print(tel1[:7]) # print(tel1[:lent(tel1)-4])
print(tel2[:9]) # print(tel2[:len(tel2)-4])