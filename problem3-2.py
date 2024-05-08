# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
visited = [[False] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
visited[x][y] = True  # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
map_data = []
for i in range(n):
    map_data.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction = (direction - 1) % 4

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하고 바다가 아닌 경우 이동
    if not visited[nx][ny] and map_data[nx][ny] == 0:
        visited[nx][ny] = True
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if map_data[nx][ny] == 0:
            x, y = nx, ny
            turn_time = 0
        else:
            break

print(count)
