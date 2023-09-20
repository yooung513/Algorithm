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
# BFS
import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
land = []   # 땅의 높이
top = 0     # 가장 높은 땅의 높이
for _ in range(n):
    tmp = list(map(int, input().split()))
    top = max(top, max(tmp))
    land.append(tmp)

dq = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

safe = [0]*(top+1)
for rain in range(2, top+1):
    chk = [[0]*n for _ in range(n)]
    cnt = 0

    for i in range(n):  # 탐색
        for j in range(n):
            if land[i][j] > rain and chk[i][j] == 0:
                cnt += 1
                dq.append((i, j))

                while dq:   # 영역 탐색
                    now = dq.popleft()
                    x = now[0]
                    y = now[1]

                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]

                        if 0<=xx<n and 0<=yy<n and land[xx][yy]>rain and chk[xx][yy]==0:
                            chk[xx][yy] = 1
                            dq.append((xx, yy))
    
    safe[rain] = cnt    # 안전영역 개수 입력

print(max(safe))    # 안전한 영역 최대 개수 출력

# DFS
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)    # 재귀함수 시간 제한


def Solve(rain, x, y):
    chk[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<n and land[xx][yy] > rain and chk[xx][yy]==0:
            Solve(rain, xx, yy)


n = int(input())
land = []   # 땅의 높이
top = 0     # 가장 높은 땅의 높이
for _ in range(n):
    tmp = list(map(int, input().split()))
    top = max(top, max(tmp))
    land.append(tmp)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

safe = 0
for rain in range(2, top+1):
    chk = [[0]*n for _ in range(n)]
    cnt = 0

    for i in range(n):  # 탐색
        for j in range(n):
            if land[i][j] > rain and chk[i][j] == 0:
                cnt += 1
                Solve(rain, i, j)
    
    safe = max(safe, cnt)
                

print(safe)    # 안전한 영역 최대 개수 출력



# 토마토
# 전체 다 익는 경우만 확인함 -> 수정 필요
import sys
input = sys.stdin.readline

from collections import deque


# 인접 토마토 영향
def Solve(x, y):
    chk[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<m and tomato[xx][yy]==0 and chk[xx][yy]==0:
            tomato[xx][yy] = 1
    


# m : 가로 칸의 수 -> 열
# n : 세로 칸의 수 -> 행
m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
chk = [[0]*m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dq = deque()

day = -1    # 하루가 지나야 영향을 받음
while True:
    flag = 'N'

    # 전체 탐색
    for i in range(n):  
        for j in range(m):
            if tomato[i][j]==1 and chk[i][j]==0:
                flag='Y'
                dq.append((i, j))

    # 인접 토마토
    while dq:
        now = dq.popleft()
        x = now[0]
        y = now[1]
        Solve(x, y)
    
    if flag == 'N':
        break
    else:
        day += 1
    
print(day)

# 수정 및 다른 방법 풀이
import sys
input = sys.stdin.readline

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
day = [[0]*m for _ in range(n)]
dq = deque()

# 초기 익은 토마토 확인
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            dq.append((i, j))

# 인접 토마토 영향 + 날짜 
while dq:
    tmp = dq.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]

        if 0<=x<n and 0<=y<m and tomato[x][y]==0:
            tomato[x][y] = 1
            day[x][y] = day[tmp[0]][tmp[1]]+1
            dq.append((x, y))

flag = 'Y'
# 최종 결과 확인
for i in range(n):
    for j in range(m):
        # 익지 않은 토마토가 있는 경우
        if tomato[i][j] == 0:
            flag = 'N'

res = 0     # 최종 날짜
if flag == 'Y':     # 전체 다 익은 경우
    for i in range(n):
        for j in range(m):
            if day[i][j] > res:
                res = day[i][j]

    print(res)
    
else:               # 안 익은 토마토가 있는 경우
    print(-1)



# 사다리 타기
import sys
input = sys.stdin.readline


def Solve(x, y):
    global flag

    if x == 9:
        if ladder[x][y] == 2:
            flag = 2

    else:
        chk[x][y] = 1
        for i in range(3):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<10 and 0<=yy<10 and ladder[xx][yy] != 0 and chk[xx][yy] == 0:
                Solve(xx, yy)
                break


ladder = [list(map(int, input().split())) for _ in range(10)]

#왼쪽 > 오른쪽 > 아래쪽
dx = [0, 0, 1]
dy = [-1, 1, 0]
flag = 0

for i in range(10):
    chk = [[0]*10 for _ in range(10)]

    if ladder[0][i] == 1:
        Solve(0, i)
    
    if flag == 2:
        print(i)
        break


# 역으로 가는 경우
import sys
input = sys.stdin.readline


def Solve(x, y):
    chk[x][y] = 1

    if x == 0:
        print(y)

    else:
        if y-1>=0 and ladder[x][y-1]==1 and chk[x][y-1]==0:
            Solve(x, y-1)
        elif y+1<10 and ladder[x][y+1]==1 and chk[x][y+1]==0:
            Solve(x, y+1)
        else:
            Solve(x-1, y)

ladder = [list(map(int, input().split())) for _ in range(10)]
chk = [[0]*10 for _ in range(10)]

for y in range(10):
    if ladder[9][y] == 2:
        Solve(9, y)



# 피자 배달거리
import sys
input = sys.stdin.readline

def Solve(idx, s):
    global res

    if idx == m:
        sum = 0 
        for j in range(len(house)): # 집
            x1 = house[j][0]
            y1 = house[j][1]
            dis = float('inf')

            for pi in cb:   # 집과 가장 가까운 피자집 찾기
                x2 = pizza[pi][0]
                y2 = pizza[pi][1]

                dis = min(dis, abs(x1-x2)+abs(y1-y2))
            sum += dis  # 최소거리 누적

        if sum < res:   # 가장 가까운 최소거리 값 추적
            res = sum
    
    else:
        for i in range(s, len(pizza)):
            cb[idx] = i
            Solve(idx+1, i+1)


n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

house = []
pizza = []
cb = [0] * m    # 조합(Combination)의 경우를 저장하는 리스트
res = float('inf')  # 도시의 최소 피자배달거리

for i in range(n):
    for j in range(n):

        if city[i][j] == 1:     # 집의 좌표
            house.append((i, j))

        if city[i][j] == 2:     # 피자집의 좌표
            pizza.append((i, j))
        
Solve(0, 0)

print(res)



# 병합정렬 (후위순위 정렬)
# 분할 후 정복하는 알고리즘
def Sort(lt, rt):
    if lt < rt:
        mid = (lt+rt)//2
        Sort(lt, mid)       # 가장 작은 영역까지 분할
        Sort(mid+1, rt)

        p1 = lt
        p2 = mid+1
        tmp = []

        # 영역 대소 비교
        while p1 <= mid and p2 <= rt:
            if arr[p1] < arr[p2]:   
                tmp.append(arr[p1])
                p1 += 1
            else:
                tmp.append(arr[p2])
                p2 += 1

        # 남은 값 추가
        if p1 <= mid:   
            tmp = tmp + arr[p1:mid+1]
        if p2 <= rt:
            tmp = tmp + arr[p2:rt+1]

        # tmp값 arr에 복사
        for i in range(len(tmp)):
            arr[lt+i] = tmp[i]

arr = [23, 11, 45, 36, 15, 67, 33, 21]
Sort(0, len(arr)-1)
print(arr)



# 퀵정렬
# Pivot 값을 설정한 후 이를 기준으로 파티션 (값을 나눔)
def Sort(lt, rt):
    if lt < rt:
        inserPosition = lt
        pivot = arr[rt]

        for i in range(lt, rt):
            # pivot값을 기준으로 좌우로 정렬
            if arr[i] <= pivot:
                arr[i], arr[inserPosition] = arr[inserPosition], arr[i]
                inserPosition += 1
                
        # pivot값 위치
        arr[rt], arr[inserPosition] = arr[inserPosition], arr[rt]

        # 분할
        Sort(lt, inserPosition-1)
        Sort(inserPosition+1, rt)


arr = [23, 11, 45, 36, 15, 67, 33, 21]
Sort(0, len(arr)-1)
print(arr)