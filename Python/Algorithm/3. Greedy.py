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



# 이코테. 모험가 길드
# 나의 풀이
n = int(input())
x = list(map(int, input().split()))

x.sort()
tmp = list()
cnt = 0
for i in x:
    tmp.append(i)
    
    if len(tmp) == tmp[-1]:
       cnt += 1
       tmp.clear()
       
print(cnt) 

# 답안 예시
n = int(input())
x = list(map(int, input().split()))
x.sort()

res = 0         # 총 그룹의 수
cnt = 0         # 현재 그룹에 포함된 모험가의 수

for i in x:     # 공포도가 낮은 사람부터 하나씩 확인하기 
    cnt += 1    # 현재 그룹에 모험가를 포함시키기
    
    if cnt >= i:    # 현재 그룹에 포함한 모험가의 수가 현재 공포도 이상이라면, 그룹을 결성한다.
        res += 1    # 총 그룹의 수 증가
        cnt = 0     # 현재 그룹에 포함된 모험가의 수 초기화
        
print(res)



# 이코테. 곱하기 혹은 더하기
# 나의 풀이
s = list(map(str, input()))

ans = 0
for x in s:
    tmp = int(x)
    
    if ans <= 1 :           # 기존 값이 0 또는 1 인 경우 -> 합
        ans += tmp
    else:
        if tmp > 1:         # 추가 값이 0 또는 1이 아닌 경우 -> 곱
            ans *= tmp 
        else:               # 추가 값이 0 또는 1인 경우 -> 합
            ans += tmp  
        
print(ans)

# 답안 예시
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])
for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
        
print(result)