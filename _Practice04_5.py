k_score = int(input("국어 점수를 입력하세요 >>>"))
e_score = int(input("국어 점수를 입력하세요 >>>"))
m_score = int(input("국어 점수를 입력하세요 >>>"))
average = (k_score+e_score+m_score) / 3

if average >= 80:
    print(f'평균은 {average}점이고 결과는 합격입니다.')
else:
    print(f'평균은 {average}점이고 결과는 불합격입니다.')