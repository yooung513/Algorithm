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