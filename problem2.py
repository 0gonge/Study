#Q2. 곱하기 혹은 더하기
#idea : 곱하기가 무조건 더 크겠지 큰 수부터 곱하면 되겠구나.
#idea2 : 곱하기의 치명적인 단점 : 1과 0일 경우에 0을 곱하면 0이 되고 1을 곱하는 건, 1을 더하는게 더 숫자가 커진다.
#이 주의사항들에 유념해서 문제를 설계한다.

#입력 조건: 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S가 주어집니다. (1 ≤S의 길이 20)
#출력 조건: 첫째 줄에 만들어질 수 있는 가장 큰 수를 출력한다.

InputNumbers = list(map(int, input("숫자열을 입력하세요:")))
InputNumbers.sort(reverse=True)
length = len(InputNumbers)

if length < 1 or length >21 :
    raise ValueError("입력 숫자의 길이는 1 이상 20이하여야 합니다.")

result = InputNumbers[0]

for num in InputNumbers[1:]:
    if num <= 1:
        result += num
    else: 
        result *= num

print("가장 큰 수:", result)




