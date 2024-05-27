
n = int(input("내림차순 정렬을 위한 숫자의 갯수와, 숫자를 입력해주세요"))

numbers = []
for i in range(n):
    numbers.append(int(input()))

numbers = sorted(numbers, reverse = True)

for i in numbers:
    print(i, end = ' ')

