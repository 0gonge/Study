# Q1. 모험가 길드
# 여행자 변수 - member_n / 공포도 변수 - member_r
member_n = int(input("모험가 수를 입력하세요: "))
if member_n <= 0 or member_n > 100000:
    raise ValueError("모험가 수는 1명 이상, 100000명 이하여야 합니다.")

member_r = list(map(int, input("모험가 각각의 공포도를 입력하세요: ").split()))

if len(member_r) > member_n:
    raise ValueError("입력된 공포도의 수가 여행자 수보다 많습니다.")

member_r.sort()

group = 0
grouped = 0

for fear in member_r:
    grouped += 1
    if grouped >= fear:
        group += 1
        grouped = 0

print("총 그룹의 수는 {}입니다.".format(group))
