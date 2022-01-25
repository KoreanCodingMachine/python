print("한 박스에 20개의 라면을 담을 수 있습니다.")
print("라면의 개수를 입력하시면 필요한 박스 수를 알려드립니다.")
ramen_num = int(input("라면의 개수를 입력하세요.>>>"))
ramen_box = ramen_num // 20
if (ramen_num % 20) == 0:
        ramen_box = ramen_num // 20
else:
        ramen_box += 1
print(f"50개 라면을 담으려면 {ramen_box}박스가 필요합니다.")
