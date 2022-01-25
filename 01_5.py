'''
    split() 함수
    문자열.split()
    문자열.split('구분자')
    문자열.split('구분자', 분할횟수)
    문자열.split(sep='구분자', maxsplit=분할횟수)

    문자열.split(sep, maxsplit) 함수는 문자열을 maxsplit 횟수만큼
    sep의 구분자를 기준으로 문자열을 구분하여 잘라서 리스트로 만들어 줍니다.

    - sep 파라미터
    해당 파라미터의 기본값은 none이며, 이때 동작은 띄어쓰기, 엔터를 구분자로 하여 문자열을 자릅니다.
    문자열.split(sep=',') 이라 한다면 문자열에서 "," 를 기준으로 자르게 됩니다.
    sep은 생략하고 문자열.split(',')으로 사용해도 무방합니다.

    - maxsplit 파라미터
    해당 파라미터의 기본값은 -1 이며, 이때 동작은 제한없이 자를 수 있을 때 까지 문자열 전체를 자릅니다.
    문자열.split(maxsplit=1) 이라 하면, 문자열을 1번만 자르게 됩니다.
    역시 maxsplit 를 생략이 가능하지만 앞에 sep 파라미터가 있어야지만 가능합니다.
    문자열.split(1) 불가능
    문자열.split(',', 1) 가능
    문자열.split(maxsplit=1) 가능 -> 문자열.spllit(sep=none,maxsplit=1)
'''

A,B = input().split() # 엔터 혹은 스페이스바를 기준으로 자를 수 있을 떄 까지 문자열 전체를 자른다.
print(int(A)+int(B))