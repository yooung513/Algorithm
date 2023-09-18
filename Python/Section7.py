# Section7. Dynamic Programming 동적계획법

# 네트워크 선 자르기
# Bottom-Up 방식
n = int(input())
res = [0]*(n+1)
res[1] = 1
res[2] = 2

for i in range(3, n+1):
    res[i] = res[i-1] + res[i-2]

print(res[n])

# Top-down 방식
def Solve(n):
    if n <= 2:
        return n
    else:
        return Solve(n-1) + Solve(n-2)

n = int(input())

print(Solve(n))



# 도전과제_계단 오르기
def Solve(n):
    if n <= 2:
        return n

    else:
        return Solve(n-1) + Solve(n-2)
    
n = int(input())

print(Solve(n))



# 도전과제_돌다리 건너기
n = int(input())
res = [0]*(n+1)
res[0] = 1
res[1] = 2

for i in range(2, n+1):
    res[i] = res[i-2] + res[i-1]

print(res[n])



# 최대 부분 증가수열
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
res = [0]*n

for i in range(n):
    tmp = []
    tmp.append(arr[i])
    
    for j in range(i+1, n):
        if arr[j] > tmp[-1]:
            tmp.append(arr[j])
    
    res[i] = len(tmp)

print(max(res))

# LIS 알고리즘
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)

lis = [0]*(n+1)
lis[1] = 1
res = 0

# 작은 값 부터 큰 값으로 풀어나가면서 메모하기
for i in range(2, n+1):
    max = 0     # 자신의 앞에서 기록된 만들 수 있는 최대 증가 수열
    
    # 이전 값 확인
    for j in range(i-1, 0, -1):
        if arr[i] > arr[j] and lis[j] > max:
            max = lis[j]
            
    lis[i] = max+1  # 자기 자신을 최종 수열에 더한 값

    # 최대 길이 수열 확인
    if lis[i] > res:
        res = lis[i]

print(res)



# 최대 선 연결하기 (LIS 응용)
# 원리가 최대 증가수열과 동일
n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)

res = [0]*(n+1)
res[1] = 1

ans = 0
for i in range(2, n+1):
    max = 0

    for j in range(i-1, 0, -1):
        if arr[i] > arr[j] and res[j] > max:
            max = res[j]
    
    res[i] = max + 1

    if res[i] > ans:
        ans = res[i]

print(ans)



# 가장 높은 탑 쌓기
import sys
input = sys.stdin.readline

n = int(input())
bricks = list(list(map(int, input().split())) for _ in range(n))
bricks.sort(key= lambda x : (-x[0], x[1], x[2]))

res = [0]*n
res[0] = bricks[0][1]
highest = res[0]

for i in range(1, n):
    # i의 최대 높이를 저장하기 위한 변수
    tmp = 0

    # 자기 자신의 앞에서 가져올 수 있는 최대 높이
    for j in range(i-1, -1, -1):
        if bricks[i][2] < bricks[j][2] and res[j] > tmp:
            tmp = res[j]

    # 자기 자신의 최대 높이
    res[i] = tmp + bricks[i][1]

    # 가장 높이 쌓을 수 있는 탑의 높이
    if res[i] > highest:
        highest = res[i]

print(highest)



# 알리바바와 40인의 도둑
from collections import deque

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = [[0]*n for _ in range(n)]

res[0][0] = arr[0][0]
dq = deque()
dq.append((0, 0))

dx = [0, 1]
dy = [1, 0]

while dq:
    tmp = dq.popleft()
    now = res[tmp[0]][tmp[1]]

    for i in range(2):
        x = tmp[0]+dx[i]
        y = tmp[1]+dy[i]

        if 0<=x<n and 0<=y<n:
            dq.append((x, y))

            if res[x][y] == 0:
                res[x][y] = arr[x][y] + now
            else:
                res[x][y] = min(res[x][y], arr[x][y] + now)
            
print(res[n-1][n-1])

# Top-Down
import sys
input = sys.stdin.readline

def Solve(x, y):
    if res[x][y] > 0:
        return res[x][y]
    
    if x == 0 and y == 0:
        return arr[0][0]
    
    else:
        if y == 0:
            res[x][y] = Solve(x-1, y)+arr[x][y]
        elif x == 0:
            res[x][y] = Solve(x, y-1)+arr[x][y]
        else:
            res[x][y] = min(Solve(x-1, y), Solve(x, y-1)) + arr[x][y]
        return res[x][y]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = [[0]*n for _ in range(n)]

print(Solve(n-1, n-1))



# 가방문제
# 냅색 알고리즘
import sys
input = sys.stdin.readline

n, tot = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(n)]
res = [0]*(tot+1)

for i in range(n):
    w = bag[i][0]
    v = bag[i][1]

    for j in range(1, tot+1):
        if 0<= j-w <= tot:
            res[j] = max(res[j-w]+v, res[j])

print(res[tot])

# 보석의 무게와 가치를 카운팅하면서 바로 체크하기
n, tot = map(int, input().split())
res = [0]*(tot+1)

for i in range(n):
    w, v = map(int, input().split())

    for j in range(w, tot+1):
        res[j] = max(res[j], res[j-w]+v)

print(res[tot])



# 동전 교환
import sys
input = sys.stdin.readline

n = int(input())
coin = list(map(int, input().split()))
m = int(input())
res = [500]*(m+1)
res[0] = 0

for i in range(n):
    c = coin[i]
    for j in range(c, m+1):
        res[j] = min(res[j], res[j-c]+1)

print(res)
print(res[m])



# 최대점수 구하기
# 한 유형 당 한 문제만 풀 수 있기 때문에 뒤에서부터 카운팅해서 중복 문제를 해결
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
res = [0]*(m+1)

for _ in range(n):
    s, t = map(int, input().split())

    for i in range(m, t-1, -1):
        res[i] = max(res[i], res[i-t]+s)
    
    print(res)

print(res[m])



# 플로이드 워샬 알고리즘
# 그래프의 최단 거리
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
city = [[5000]*(n+1) for _ in range(n+1)]

# 초기값 설정
for i in range(1, n+1):
    city[i][i] = 0

for _ in range(m):
    s, e, v = map(int, input().split())
    city[s][e] = v


# 최소값으로 설정
# 중간 노드를 지나가는 값을 설정해 꾸준히 최소로 유지
for m in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            city[s][e] = min(city[s][e], city[s][m]+city[m][e])

# 값 출력
for x in range(1, n+1):
    for y in range(1, n+1):
        if city[x][y] == 5000:
            print('M', end=' ')
        else:
            print(city[x][y], end=' ')
    print()



# 회장뽑기
# 플로이드-워샬 알고리즘 응용
import sys
input = sys.stdin.readline

n = int(input())
man = [[50]*(n+1) for _ in range(n+1)]

# 초기 세팅
for i in range(1, n+1):
    man[i][i] = 0

while True:
    a, b = map(int, input().split())
    if a < 0 and b < 0:
        break
    else:
        man[a][b] = 1
        man[b][a] = 1


# 최소값 유지
for m in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            man[s][e] = min(man[s][e], man[s][m]+man[m][e])


# 결과 값 추출
res = [0]*(n+1)
sco = 50
for x in range(1, n+1):
    tmp = 0
    for y in range(1, n+1):
        if tmp < man[x][y]:
            tmp = man[x][y]

    if sco > tmp:
        sco = tmp
    
    res[x] = tmp

print(sco, res.count(sco))
for r in range(1, n+1):
    if res[r] == sco:
        print(r, end=' ')



# 위상정렬
# 그래프 정렬
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
order = [0]*(n+1)

for _ in range(m):
    s, e = map(int, input().split())
    order[e] += order[s]+1

res = []
for idx, val in enumerate(order):
    if idx > 0:
        res.append((val, idx))

res.sort()
for x in res:
    print(x[1], end=' ')