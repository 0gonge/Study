n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key= lambda student : student[1])

for student in array:
    print(student[0], end= ' ')

n = int(input())

# array = []
# for i in range(n):
#     input_data = input().split()
#     array.append((input_data[0], int(input_data[1])))
#
# # 점수를 반환하는 함수 정의
# def get_score(student):
#     return student[1]
#
# # 정렬 시 람다 대신 함수 사용
# array = sorted(array, key=get_score)
#
# for student in array:
#     print(student[0], end=' ')
