#두개의 배열을 받아서 A배열의 요소들의 합이 최대가 될 수 있도록 한다.
#N만큼 입력 받을 수 있고, K번 바꿀 수 있다.

n, k = map(int, input().split())

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

list_a.sort() #defult = 오름차순
list_b.sort(reverse=True) #내림차순

#첫 번째 인덱스부터 확인하면서 두 배열의 원소를 최대 K번 비교

for i in range(k):
    if list_a[i] < list_b[i]:
        list_a[i], list_b[i] = list_b[i] , list_b[i]
    else:
        break
print(sum(list_a))

