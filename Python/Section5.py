# Section5. 완전탐색 (DFS 기초)


# 재귀함수를 이용한 이진수 출력
# 왜 %가 나오지..?
def Solve(n):
    if n < 2:
        ans.append(n)
        return 
    m = n%2
    ans.append(m)
    Solve(n//2)


n = int(input())
ans = []
Solve(n)

for i in range(len(ans)-1, -1, -1):
    print(ans[i], end="")

# 수정
# 코드에서는 %가 출력되나 다른 ide에서는 출력되지 않음
def Solve(n):
    if n == 0:
        return
    else:
        Solve(n//2)
        print(n%2, end='')

n = int(input())
Solve(n)



# 이진트리순회 (DFS)
# 1. 전위순회 출력
def DFS(n):
    if n >= 8:
        return 
    print(n, end=' ')
    DFS(n*2)
    DFS((n*2)+1)

DFS(1)

# 2. 중위순회 출력
def DFS(n):
    if n >= 8:
        return 
    DFS(n*2)
    print(n, end=' ')
    DFS((n*2)+1)

DFS(1)

# 3. 후위순회 출력
def DFS(n):
    if n >= 8:
        return 
    DFS(n*2)
    DFS((n*2)+1)
    print(n, end=' ')

DFS(1)



# 부분집합 구하기 (DFS)
def DFS(x):
    if x > n:
        for a in ans:
            print(a, end=' ')
        print()
        return
    else:
        ans.append(x)
        DFS(x+1)
        ans.pop()
        DFS(x+1)


n = int(input())
ans = []
DFS(1)

# 추가
def DFS(x):
    if x > n:
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
        return
    else:
        ch[x] = 1
        DFS(x+1)
        ch[x] = 0
        DFS(x+1)

n = int(input())
ch = [0]*(n+1)
DFS(1)



# 합이 같은 부분집합
def DFS(L, s):
    if ans[0] > 0:
        return
    
    if L >= n:
        if total == s*2:
            ans[0] += 1
        return
    else:
        DFS(L+1, s+num[L])
        DFS(L+1, s)


n = int(input())
num = list(map(int, input().split()))
total = sum(num)
ans = [0]

DFS(0, 0)

if ans[0] > 0:
    print('YES')
else:
    print('NO')

# 추가
import sys

def DFS(L, sum):
    if sum > total // 2:
        return
    
    if L == n:
        if total == sum*2:
            print('YES')
            sys.exit(0)
    else:
        DFS(L, sum+1)
        DFS(L, sum)

n = int(input())
num = list(map(int, input().split()))
total = sum(num)
DFS(0, 0)
print('NO')



# 바둑이 승차
import sys
input = sys.stdin.readline

def DFS(L, s):
    global res
    
    if s > c:
        return
    
    if L == n:
        if s > res:
            res = s
        return
    else:
        DFS(L+1, s+w[L])
        DFS(L+1, s)


c, n = map(int, input().split())
w = [int(input()) for _ in range(n)]
res = 0
DFS(0, 0)
print(res)

# 시간초과 수정
# 조건에 의해 최대 무게를 구해야 하므로 중간 단계에서 구한 값보다 작은 경우 계산하지 않음
import sys
input = sys.stdin.readline

def DFS(L, s, tsum):
    global res
    
    if s + (total-tsum) < res:
        return

    if s > c:
        return
    
    if L == n:
        if s > res:
            res = s
        return
    else:
        DFS(L+1, s+w[L], tsum+w[L])
        DFS(L+1, s, tsum+w[L])


c, n = map(int, input().split())
w = [int(input()) for _ in range(n)]
total = sum(w)
res = 0
DFS(0, 0, 0)
print(res)



# 중복순열 구하기
def DFS(L):
    global cnt

    if L == m:
        print(*chk)
        cnt += 1
        return
    
    else:
        for i in range(1, n+1):
            chk[L] = i
            DFS(L+1)


n, m = map(int, input().split())
chk = [0]*m
cnt = 0
DFS(0)
print(cnt)



# 동전교환
import sys
input = sys.stdin.readline

def Solve(idx, now, cnt):
    global res 
    
    if cnt > res:
        return 
    
    if idx == n or now == 0:
        if res > cnt:
            res = cnt
        return 
    
    else:
        cnt = now//coin[idx]
        now %= coin[idx]
        Solve(idx+1, now, cnt)


n = int(input())
coin = list(map(int, input().split()))
coin.sort(reverse=True)
m = int(input())
res = float('inf')
Solve(0, m, 0)
print(res)

# 다른 풀이
def DFS(cnt, sum):
    global res

    if cnt > res:   # 최소 개수 찾기
        return
    
    if sum > m:     # 거슬러 줄 돈 초과
        return
    
    if sum == m:
        if cnt < res:
            res = cnt

    else:           # 거슬러 줄 돈이 남은 경우
        for i in range(n):
            DFS(cnt+1, sum+coin[i])


n = int(input())
coin = list(map(int, input().split()))
m = int(input())

res = float('inf')
coin.sort(reverse=True)
DFS(0, 0)



# 순열 구하기
def Solve(idx):
    global cnt
    
    if idx == m:
        print(*ans)
        cnt += 1
        return
    
    else:
        for i in range(1, n+1):
            if chk[i] == 0:
                chk[i] = 1
                ans[idx] = i
                Solve(idx+1)
                chk[i] = 0


n, m = map(int, input().split())
ans = [0]*m         # 순열
chk = [0]*(n+1)     # 중복체크용
cnt = 0     

Solve(0)
print(cnt)



# 순열 추측하기
import sys
from collections import deque

def Solve(idx):
    if idx == n:
        tmp = 0
        dq = deque(ans)
        while dq:
            for _ in range(len(dq)-1):
                x = dq.popleft()
                y = dq.popleft()
                dq.append(x+y)
                dq.appendleft(y)
            tmp = dq.popleft()

        if tmp == f:
            print(*ans)
            sys.exit(0)
    
    else:
        for i in range(1, n+1):
            if chk[i] == 0:
                chk[i] = 1
                ans[idx] = i
                Solve(idx+1)
                chk[i] = 0


n, f = map(int, input().split())
chk = [0]*(n+1)
ans = [0]*n
Solve(0)


# 이항계수 사용
import sys

def DFS(L, sum):
    if L == n and sum == f:
        for x in p:
            print(x, end=' ')
        sys.exit(0)         # 최초의 경우만 출력

    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                DFS(L+1, sum + (p[L]*b[L]))
                ch[i] = 0


n, f = map(int, input().split())
b = [1]*n       # 이항계수
p = [0]*n       # 구한 순열 값 
                # 동일 인덱스, 이항계수 * 구한 순열값 => 파스칼 삼각형의 합 
ch = [0]*(n+1)  # 중복 방지용

# 이항계수 구하기
for i in range(1, n):   # 이항계수의 양 끝은 1이므로
    b[i] = b[i-1]*(n-i)//i  # 조합 값 : 앞의 값 * (nCr의 n값 == 입력받은 n-i값) // 1부터 nCr의 n까지의 값
    
# 순열 구하기
DFS(0, 0)


# 라이브러리 사용
import itertools as it

n, f = map(int, input().split())
b = [1]*n   # 이항계수
cnt = 0

# 이항계수 구하기 
for i in range(1, n):
    b[i] = b[i-1] * (n-i) // i

# 자연수 범위 값 (순열의 원소 값)
a = list(range(1, n+1))

# 순열 생성
for tmp in it.permutations(a):
    sum = 0
    for idx, val in enumerate(tmp):
        sum += val * b[idx]     # 파스칼 삼각형 합
    
    if sum == f:
        for x in tmp:
            print(x, end=' ')
        break



# 조합 구하기
# 재귀함수 사용
def Solve(idx, now):
    global cnt 

    if idx == m:
        cnt += 1
        print(*ans)
        return

    else:
        for i in range(now, n+1):
            ans[idx] = i
            Solve(idx+1, i+1)

n, m = map(int, input().split())
ans = [0]*m
cnt = 0

Solve(0, 1)
print(cnt)

# 라이브러리 사용
import itertools as it

n, m = map(int, input().split())

cnt = 0
for tmp in it.combinations(range(1, n+1), m):
    cnt += 1
    print(*tmp)
print(cnt)



# 인접행렬 (가중치 그래프)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0]*n for _ in range(n)]

for _ in range(m):
    s, e, w = map(int, input().split())
    arr[s-1][e-1] = w

for x in arr:
    print(*x)



#무방향 그래프 인접행렬
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    arr[s][e] += 1
    arr[e][s] += 1

for i in range(1, n+1):
    for j in range(1, n+1):
        print(arr[i][j], end=' ')
    print()



# 경로 탐색
import sys 
iuput = sys.stdin.readline

def Solve(v):
    global cnt 

    if v == n:      # 종착 노드에 도착
        cnt += 1

    else:
        # 인접 노드로 이동
        for i in range(1, n+1):
            if arr[v][i] == 1 and chk[i] == 0:
                chk[i] = 1
                Solve(i)
                chk[i] = 0
    

n, m = map(int, input().split())
arr = [[0]*(n+1) for _ in range(n+1)]
chk = [0]*(n+1) # 중복 방지용

for _ in range(m):
    s, e = map(int, input().split())
    arr[s][e] += 1

cnt = 0
chk[1] = 1
Solve(1)

print(cnt)



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



