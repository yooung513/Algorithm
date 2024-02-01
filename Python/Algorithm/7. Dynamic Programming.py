# 동적 계획법

# 백준 2839. 설탕 배달
n = int(input())

dy = [0]*(n+1)
dy[1], dy[2] = 5000, 5000

for i in range(3, n+1):
    if i >= 5:
        dy[i] = min(dy[i-3], dy[i-5]) + 1
    else:
        dy[i] = dy[i-3] + 1
        
if dy[n] >= 5000:
    print(-1)
else:
    print(dy[n])
    
    
    
# 이코테. 1로 만들기
d = [0] * 30001
d[1] = 0
d[2] = 1
d[3] = 1
d[4] = 2
d[5] = 1

x = int(input())
for i in range(6, x+1):
    tmp = 30001
    if i % 5 == 0:
        tmp = min(tmp, d[i//5]+1)
        
    if i % 3 == 0:
        tmp = min(tmp, d[i//3]+1)
        
    if i % 2 == 0:
        tmp = min(tmp, d[i//2]+1)
        
    tmp = min(tmp, d[i-1]+1)
    d[i] = tmp
    
print(d[x])


# 답안 예시
x = int(input())
dp = [0] * 30001

# 바텀업 방식 Dynamic Programming
for i in range(2, x+1):
    dp[i] = dp[i - 1] + 1
    
    if i % 2 == 0: 
        dp[i] = min(dp[i], dp[i // 2] + 1)
        
    if i % 3 == 0: 
        dp[i] = min(dp[i], dp[i // 3] + 1)
        
    if i % 5 == 0: 
        dp[i] = min(dp[i], dp[i // 5] + 1)
        
print(dp[x])



# 이코테. 개미전사
n = int(input())
k = list(map(int, input().split()))
dp = [0] * n

dp[0] = k[0]
dp[1] = max(k[0], k[1])

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + k[i])
    
print(dp[n-1])