# 최대 점수 구하기
import sys 
iuput = sys.stdin.readline

def Solve(idx, sco, time):
    global res

    if time > m:
        return
    
    if idx == n:
        if sco > res:
            res = sco
            return

    else:
        Solve(idx+1, sco+arr[idx][0], time+arr[idx][1])
        Solve(idx+1, sco, time)

   

n, m = map(int, input().split())
arr = []
for _ in range(n):
    s, t = map(int, input().split())
    arr.append((s, t))

res = 0

Solve(0, 0, 0)
print(res)



# 휴가
import sys
input = sys.stdin.readline

def Solve(idx, sum):
    global res

    if idx >= n:
        if sum > res:
            res = sum

    else:
        date = arr[idx][0]
        pay = arr[idx][1]

        # 상담을 하는 경우
        Solve(idx+date, sum+pay)

        #상담을 하지 않는 경우
        Solve(idx+1, sum)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = 0

Solve(0, 0)
print(res)

# 중간에 상담일이 휴가보다 긴 경우는 고려하지 않음으로 cut 할 수 있다.
# if idx+date <= n: 



# 양팔저울
import sys
input = sys.stdin.readline


def Solve(idx, sum):
    if idx == k:
        if 0 <= sum <= s:
            chk[sum] = 0
    else:
        # 저울의 왼쪽에 추를 올려놓음
        Solve(idx+1, sum+w[idx])

        # 저울의 오른쪽에 추를 올려놓음
        Solve(idx+1, sum-w[idx])

        # 저울에 추를 올려놓지 않음
        Solve(idx+1, sum)


k = int(input())
w = list(map(int, input().split()))
s = sum(w)
chk = [1]*(s+1)
chk[0] = 0

Solve(0, 0)
print(sum(chk))

# set을 활용하는 방법
import sys
input = sys.stdin.readline


def Solve(idx, sum):
    global res

    if idx == k:
        if 0 < sum <= s:    # 양수인 경우에만 값 입력
            res.add(sum)

    else:
        # 저울의 왼쪽에 추를 올려놓음
        Solve(idx+1, sum+w[idx])

        # 저울의 오른쪽에 추를 올려놓음
        Solve(idx+1, sum-w[idx])

        # 저울에 추를 올려놓지 않음
        Solve(idx+1, sum)


k = int(input())
w = list(map(int, input().split()))
s = sum(w)
res = set()

Solve(0, 0)
print(s-len(res))



# 동전 바꿔주기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


def Solve(idx, sum):
    global cnt
    if sum > t:
        return
    
    if idx == k:
        if sum == t:
            cnt += 1

    else:
        p = coin[idx][0]
        n = coin[idx][1]
        for i in range(n+1):
            Solve(idx+1, sum+(p*i))


t = int(input())    # 지폐의 금액
k = int(input())    # 동전의 가지수
coin = [list(map(int, input().split())) for _ in range(k)]  # 동전 (금액, 개수)
cnt = 0     # 교환 방법 카운트

Solve(0, 0)

print(cnt)



# 알파코드
def Solve(idx, p):
    global cnt

    if idx == n:    # 종착노드 도달
        cnt += 1
        for j in range(p):  # res값에서 필요한 부분만 추출
            print(chr(res[j]+64), end='')
        print()
    
    else:
        for i in range(1, 27):  # 사전 순으로 출력
            if code[idx] == i:  # 한자리 수
                res[p] = i
                Solve(idx+1, p+1)

            elif i >= 10 and code[idx] == i//10 and code[idx+1] == i%10 :   # 두자리 수
                res[p] = i
                Solve(idx+2, p+1)

code = list(map(int, input()))
n = len(code)   # 종착노드
code.append(-1) # 범위 오류 방지용
res = [0]*n
cnt = 0

Solve(0, 0)

print(cnt)



# 송아지 찾기
from collections import deque

s, e = map(int, input().split())
res = [0]*10001
jump = [1, -1, 5]
dq = deque()
dq.append(s)

while dq:
    now = dq.popleft()

    if now == e:
        print(res[now])
        break

    else:
        for i in range(3):
            next = now + jump[i]
            res[next] = res[now] + 1
            dq.append(next)

# 이미 갔던 곳 체크해서 없애기, 점프 표현 다르게 하기
from collections import deque

s, e = map(int, input().split())
chk = [0]*10001
res = [0]*10001
chk[s] = 1

dq = deque()
dq.append(s)

while dq:
    now = dq.popleft()

    if now == e:
        print(res[now])
        break

    else:
        for next in (now+1, now-1, now+5):
            if 0 < next <= 10000:
                if chk[next] == 0:
                    chk[next] = 1
                    res[next] = res[now]+1
                    dq.append(next)



# 사과나무
import sys
input = sys.stdin.readline


def Solve(num, x, y):
    global res

    if num == (n//2)+1:
        return
    
    else:
        if chk[x][y] == 0:
            chk[x][y] = 1
            res += tree[x][y]
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                Solve(num+1, xx, yy)


n = int(input())

tree = [list(map(int, input().split())) for _ in range(n)]
chk = [[0]*n for _ in range(n)]
res = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

Solve(0, n//2, n//2)
print(res)

# Queue 활용하기
import sys
input = sys.stdin.readline

from collections import deque


n = int(input())
tree = [list(map(int, input().split())) for _ in range(n)]
chk = [[0]*n for _ in range(n)]
res = 0
dq = deque()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dq.append((n//2, n//2))
chk[n//2][n//2] = 1
res += tree[n//2][n//2]
num = 0

while True:
    if num == n//2:
        break

    size = len(dq)

    for _ in range(size):
        tmp = dq.popleft()

        for i in range(4):
            x = tmp[0] + dx[i]
            y = tmp[1] + dy[i]

            if chk[x][y] == 0:
                chk[x][y] = 1
                res += tree[x][y]
                dq.append((x, y))
    
    num += 1

print(res)    



# 미로의 최단거리 통로
import sys
input = sys.stdin.readline

def Solve(cnt, x, y):
    global res
    
    if x == 6 and y == 6:
        res = min(res, cnt)
        return

    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < 7 and 0 <= yy < 7 and maze[xx][yy] == 0:
                maze[xx][yy] = 1
                Solve(cnt+1, xx, yy)
                maze[xx][yy] = 0

maze = [list(map(int, input().split())) for _ in range(7)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

res = float('inf')
maze[0][0] = 1
Solve(0, 0, 0)

if res == float('inf'):
    print(-1)
else:
    print(res)

# Queue 사용하기
import sys
input = sys.stdin.readline

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

maze = [list(map(int, input().split())) for _ in range(7)]
dis = [[0]*7 for _ in range(7)]

dq = deque()
dq.append((0, 0))
maze[0][0] = 1

while dq:
    tmp = dq.popleft()

    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]

        if 0 <=x<7 and 0<=y<7 and maze[x][y] == 0:
            maze[x][y] = 1
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1
            dq.append((x, y))
    
if dis[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])



# 미로탐섹
import sys
input = sys.stdin.readline


def Solve(x, y):
    global cnt 

    if x == 6 and y == 6:
        cnt += 1

    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            
            if 0 <=xx<7 and 0<=yy<7 and maze[xx][yy] == 0:
                maze[xx][yy] = 1
                Solve(xx, yy)
                maze[xx][yy] = 0

maze = [list(map(int, input().split())) for _ in range(7)]
maze[0][0] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0

Solve(0, 0)

print(cnt)



# 등산경로
import sys
input = sys.stdin.readline


def Solve(x, y):
    global cnt

    if x == highx and y == highy:
        cnt += 1

    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<n and 0<=yy<n and road[x][y] < road[xx][yy]:
                Solve(xx, yy)
        

n = int(input())
road = [list(map(int, input().split())) for _ in range(n)]

row = float('inf')
rowx, rowy = 0, 0

high = float('inf') * -1
highx, highy = 0, 0

for i in range(n):
    for j in range(n):
        if row > road[i][j]:
            row = road[i][j]
            rowx, rowy = i, j
        
        if high < road[i][j]:
            high = road[i][j]
            highx, highy = i, j

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0

Solve(rowx, rowy)

print(cnt)



# 단지 번호 붙이기
import sys
input = sys.stdin.readline

from collections import deque

def Solve(x, y):
    dq = deque()
    dq.append((x, y))

    cnt = 0
    while dq:
        now = dq.popleft()
        x = now[0]
        y = now[1]
        if apart[x][y] == 1:
            apart[x][y] = 0
            cnt += 1

            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if 0<=xx<n and 0<=yy<n and apart[xx][yy] == 1:
                    dq.append((xx, yy))
    
    return cnt


n = int(input())
apart = [list(map(int, input().split())) for _ in range(n)]
res = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(n):
        if apart[i][j] == 1:
            ans = Solve(i, j)
            res.append(ans)

res.sort()
print(len(res))
for i in range(len(res)):
    print(res[i])

# 다른 풀이
import sys
input = sys.stdin.readline


def Solve(x, y):
    global cnt
    
    apart[x][y] = 0
    cnt += 1

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if 0<=xx<n and 0<=yy<n and apart[xx][yy] == 1:
            Solve(xx, yy)


n = int(input())
apart = [list(map(int, input().split())) for _ in range(n)]
res = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(n):
        if apart[i][j] == 1:
            cnt = 0
            Solve(i, j)
            res.append(cnt)

res.sort()
print(len(res))
for i in range(len(res)):
    print(res[i])



# 섬나라 아일랜드
# DFS
import sys
input = sys.stdin.readline


def Solve(x, y):
    island[x][y] = 0
    for i in range(8):
        xx = x + dx[i]
        yy = y + dy[i]

        if 0<=xx<n and 0<=yy<n and island[xx][yy] == 1:
            Solve(xx, yy)


dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

n = int(input())
island = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        if island[i][j] == 1:
            cnt += 1
            Solve(i, j)

print(cnt)

# BFS
import sys
input = sys.stdin.readline

from collections import deque


dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

n = int(input())
island = [list(map(int, input().split())) for _ in range(n)]
dq = deque()
cnt = 0

for i in range(n):
    for j in range(n):
        if island[i][j] == 1:
            cnt += 1
            dq.append((i, j))

            while dq:
                now = dq.popleft()
                x = now[0]
                y = now[1]
                island[x][y] = 0

                for k in range(8):
                    xx = x + dx[k]
                    yy = y + dy[k]

                    if 0<=xx<n and 0<=yy<n and island[xx][yy] == 1:
                        dq.append((xx, yy))

print(cnt)



# 안전영역
