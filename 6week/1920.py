def binary_search(array, target, start, end):
    # 이진 탐색 함수 정의
    while start <= end:
        mid = (start + end) // 2  # 중간 인덱스를 계산
        if array[mid] == target:  # 중간 값이 타겟 값과 같으면
            return True  # True 반환
        elif array[mid] > target:  # 중간 값이 타겟 값보다 크면
            end = mid - 1  # 오른쪽 부분을 버림
        else:  # 중간 값이 타겟 값보다 작으면
            start = mid + 1  # 왼쪽 부분을 버림
    return False  # 값을 찾지 못하면 False 반환

# 입력 받기
n = int(input())  # 첫 번째 줄에서 N을 입력 받음
a = list(map(int, input().split()))  # 두 번째 줄에서 N개의 정수를 입력 받음
m = int(input())  # 세 번째 줄에서 M을 입력 받음
targets = list(map(int, input().split()))  # 네 번째 줄에서 M개의 정수를 입력 받음

# 리스트 정렬
a.sort()  # 이진 탐색을 위해 리스트 A를 오름차순으로 정렬

# 각 타겟에 대해 이진 탐색 수행
results = []  # 결과를 저장할 리스트 초기화
for target in targets:
    if binary_search(a, target, 0, n - 1):  # 이진 탐색 수행
        results.append(1)  # 존재하면 1 추가
    else:
        results.append(0)  # 존재하지 않으면 0 추가

# 결과 출력
for result in results:
    print(result)  # 각 결과를 출력
