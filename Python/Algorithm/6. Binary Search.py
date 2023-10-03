# 탐색

# 백준 1236. 성 지키기
import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
castle = [list(input().strip()) for _ in range(n)]

row_need = 0
for i in range(n):
    for j in range(m):
        if castle[i][j]=='X':
            break
    else:
        row_need += 1

col_need = 0
for j in range(m):
    for i in range(n):
        if castle[i][j] == 'X':
            break
    else:
        col_need += 1

print(max(row_need, col_need))



# 백준 2110. 공유기 설치
import sys 
input = sys.stdin.readline

# 거리에 따른 공유기의 개수를 세는 함수
def Count(len):
    end = house[0]    # 제일 처음 집에 공유기 설치
    cnt = 1
    for i in range(1, n):
        if house[i]-end >= len:
            cnt += 1
            end = house[i]

    return cnt


n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

s, e = 1, house[n-1]
res = 0
while s <= e:
    mid = (s+e)//2

    if Count(mid) >= c:
        res = mid
        s = mid+1
    else:
        e = mid-1

print(res)



# 백준 1939. 중량제한
import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
island = [[0]*(n+1) for _ in range(n+1)]

max_w = 0
for _ in range(m):
    a, b, c = map(int, input())
    island[a][b] = c
    island[b][c] = c
    
    if max_w < c: 
        max_w = c

s, e = map(int, input().split())
res = 0
if island[s][e] == max_w:
    print(max_w)
else:
    for i in range(1, n+1):
        if island[s][i] != 0:
            res = max(res, Solve(s, i))

# -> 다시 풀기