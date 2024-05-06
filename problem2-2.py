# 코테 1-2번은 난이도가 가장 낮은 그리디 알고리즘이나 구현문제다.
# 난이도가 낮기 때문에 무조건 맞춰야 함.

# 일단 문제를 읽고 든 생각은, 좌표 평면이라고 생각하고 입력을 받은 공간에 계획서 대로 이동을 시켜줘야 하며,
# 공간을 벗어나는 경우 무시해주는 경우를 생각을 해주어야 한다.

# 공간의 크기 변수 - space
# planning_route - 계획을 받아줄 변수
# plans_direction - 계획들을 받아 줄 변수

space = int(input("공간의 크기를 입력해주세요"))
if space < 1 or space > 100:
    raise ValueError("공간의 크기는 1 이상 100이하여야 합니다.")

planning_route = input("계획을 입력해주세요").split()#공백으로 분리해준다.
if not (1 <= len(planning_route) <= 100): # if not으로 코드를 간략하게 해줄 수도 있구나를 알았다.
    raise ValueError("계획의 길이는 1이상 100 이하여야 합니다.")


def move_in_grid(space, planning_route):
    x, y = 1, 1 # 문제에서 초기 위치 1,1이라고 정의해두었음.
    plans_direction = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

    for move in plans_direction.split():
        # 입력된 명령이 유효한지 확인
        if move not in planning_route:
            raise ValueError(f"유효하지 않은 명령 '{move}'가 포함되어 있습니다. 유효한 명령: L, R, U, D")
            #이번엔 파일 명령처럼 정의해 보았다.

    for move in planning_route.split():

        dx, dy = plans_direction[move]
        nx, ny = x + dx, y + dy

        # 새 위치가 그리드 범위 내에 있는지 확인
        if 1 <= nx <= space and 1 <= ny <= space:
            x, y = nx, ny

    # 최종 위치 반환
    return (x, y)

# 최종 위치 계산 및 출력
final_position = move_in_grid(space, planning_route)
print("최종 위치:", final_position)

