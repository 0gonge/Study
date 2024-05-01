# 1.idea: 24시간제로 생각해야 한다.
# 2.idea: 시간에서 3이 포함된 경우의 수기 때문에 문제에서 초단위까지 주어져서 가능한 한
# 많은 경우의 수를 생각해 봤을 때, 초 단위로 생각해야 한다.
# 3.idea: 60초 X 60분 X 24 = 86400초
# 4.idea: 1씩 단순하게 증가 시키기 및 확인 -> 반복문!!

#해설을 보고 기분이 100만개 이하일 때 탐색 알고리즘을 쓰는게 좋다는 사실을 새로 알았다.

#나는 이 숫자들을 리스트형식으로 받아서 리스트 안에 3이 있나없나 확인하는 방식으로 문제를 풀고자 한다.
#3을 세어줄 변수 - count_three

#Hour - 시간 입력 변수 /

hour = int(input())
if hour < 0 or hour > 23:
    raise ValueError("0 이상 23이하의 수만 입력가능합니다.")

count_three = 0
#range는 -1까지 세어주는 것이 default이기 때문에 + 1을 해주었음.
for i in range (hour + 1):
    for j in range(60): #여기선 59초니까 상관 없음
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count_three += 1

print(count_three)
#3이 무조건 하나라도 들어가 있을 경우에 카운트니까 이렇게 쉽게 반복문으로 구현이 가능하다.