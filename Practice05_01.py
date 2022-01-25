score = int(input("점수를 입력하세요 >>> "))
school_score = ''
if 90<=score<=100:
    print(f"점수는 {score}이고, 학점은 A학점입니다.")
elif 80<=score<=89:
    print(f"점수는 {score}이고, 학점은 B학점입니다.")
elif 70<=score<=79:
    print(f"점수는 {score}이고, 학점은 C학점입니다.")
elif 60<=score<=69:
    print(f"점수는 {score}이고, 학점은 D학점입니다.")


else:
    print(f"점수는 {score}이고, 학점은 F학점입니다.")