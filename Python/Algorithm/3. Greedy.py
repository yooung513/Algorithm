# 이코테 1-그리디. 큰 수의 법칙
# 기존 풀이 - 반복문 사용
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

cnt = 0
ans = 0
while m > 0:
    if m >= k:
        ans += arr[0]*k
        ans += arr[1]
        m -= (k+1)
    else:
        ans += arr[0]*m
        break
    
print(ans)

# 수학적 구현
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
x = arr[0]  # 가장 큰 값
y = arr[1]  # 두 번째로 큰 값

ans = ((k*x + y) * (m//(k+1))) + (x*(m % (k+1)))
print(ans)



# 이코테. 숫자 카드 게임
import sys

n, m = map(int, input().split())

res = float('-INF')
for _ in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    
    if res < min(arr):
        res = min(arr)

print(res)



# 이코테. 1이 될 때 까지
n, k = map(int, input().split())

cnt = 0
while n != 1:
    if n % k == 0:
        n //= k
    else:
        n -= 1

    cnt += 1

print(cnt)