# 그래프

# 백준 2606. 바이러스
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
com = [[0]*(n+1) for _ in range(n+1)]
t = int(input())
for _ in range(t):
    s, e = map(int, input().split())
    com[s][e] = 1
    com[e][s] = 1

res = set()
dq = deque()
for i in range(2, n+1):
    if com[1][i] == 1:
        dq.append(i)
        res.add(i)

while dq:
    x = dq.popleft()
    for y in range(2, n+1):
        if com[x][y] == 1 and y not in res:
            dq.append(y)
            res.add(y)
    
print(len(res))



# 백준 1697. 숨바꼭질
from collections import deque

n, k = map(int, input().split())
dis = [0]*100001
chk = [0]*100001
chk[n] = 1
dq = deque()
dq.append(n)

while dq:
    x = dq.popleft()

    if x == k:
        break

    for i in (x-1, x+1, 2*x):
        if 0 <= i <= 100000:
            if chk[i] == 0:
                chk[i] = 1
                dis[i] = dis[x]+1
                dq.append(i)
            
print(dis[k])