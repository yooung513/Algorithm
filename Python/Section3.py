# 이분탐색 (결정 알고리즘) 및 그리디 알고리즘

# 이분검색
# 나의 풀이 -> 답만 추출할 수 있도록 함 (이분검색은 아님)
n, m = map(int, input().split())
a = list(map(int, input().split()))

res = 1
for x in a:
    if x < m :
        res += 1

print(res)

# 이분검색이란? 
# 검색할 자료를 반씩 나누어 나머지 반만 검새하는 방식을 반복하여 자료를 찾는 검색 방법
# 이분검색 : O(log n)
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

lt = 0
rt = n-1        #인덱스 값이므로

while lt <= rt:
    mid = (lt+rt) // 2 
    if a[mid] == m:
        print(mid+1)
        break
    else:
        if a[mid] > m:
            rt = mid - 1
        else:
            lt = mid + 1


# 랜선 자르기
k, n = map(int, input().split())
line = list(int(input()) for _ in range(k))

def check(n):
    cnt = 0
    for x in line:
        cnt += x//n
    return cnt

max_line = 0
lt = 0
rt = min(line)

while lt <= rt:
    mid = (lt+rt)//2
    if check(mid) >= n:
        max_line = max(max_line, mid)
        lt = mid + 1
    else:
        rt = mid - 1

print(max_line)

# 값의 범위 변화 -> 랜선 하나의 최대 길이로 해야함
import sys
input = sys.stdin.readline

def Count(L):
    cnt = 0
    for x in line:
        cnt += x//L
    return cnt

k, n = map(int, input().split())
line = [int(input()) for _ in range(k)]

lt = 1
rt = max(line)
while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= n:
        res = mid
        lt += 1
    else:
        rt -= 1
print(res)
    

# 뮤직비디오
n, m = map(int, input().split())
song = list(map(int, input().split()))

def cnt(cap):
    cnt = 0
    chk = 0
    for s in song:
        chk += s
        if chk > cap:
            cnt += 1
            chk = s
        elif chk == cap:
            cnt += 1
            chk = 0 
    if chk > 0:
        cnt += 1
    return cnt 

lt = 0
rt = sum(song)
min_cap = 2147000000
while lt <= rt:
    mid = (lt+rt)//2
    if cnt(mid) <= m:
        min_cap = min(min_cap, mid)
        rt = mid - 1
    else:
        lt = mid + 1
        
print(min_cap)

# -> 논리 문제 발생 
# 9개의 노래를 9개의 DVD에 담을 경우 최소 용량은 가장 큰 노래여야 함
n, m = map(int, input().split())
song = list(map(int, input().split()))

def cnt(cap):
    cnt = 0
    chk = 0
    for s in song:
        chk += s
        if chk > cap:
            cnt += 1
            chk = s
        elif chk == cap:
            cnt += 1
            chk = 0 
    if chk > 0:
        cnt += 1
    return cnt 

lt = max(song)
rt = sum(song)
min_cap = 2147000000
while lt <= rt:
    mid = (lt+rt)//2
    if cnt(mid) <= m:
        min_cap = min(min_cap, mid)
        rt = mid - 1
    else:
        lt = mid + 1
        
print(min_cap)
# lt의 범위 변경



# 마구간 정하기 (결정 알고리즘)
import sys
input = sys.stdin.readline

def Count(L):
    cnt = 1
    ep = x[0]
    for i in range(1, n):
        if x[i] - ep >= L:
            cnt += 1
            ep = x[i]
    return cnt



n, c = map(int, input().split())
x = [int(input()) for _ in range(n)]
x.sort()

lt = 1
rt = x[-1]
res = 0
while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= c:
        res = mid
        lt = mid+1
    else:
        rt = mid-1

print(res)



# 회의실 배정 (그리디)
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
time.sort(key= lambda x : x[1])

can = []
for x in time:
    if len(can) == 0:
        can.append(x)
    else:
        s = x[0]
        if can[-1][1] <= s:
            can.append(x)

print(len(can))



# 씨름선수 (그리디)
import sys
input = sys.stdin.readline

n = int(input())
men = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(n):
    if any(men[i][0] < men[x][0] and men[i][1] < men[x][1] for x in range(n)):
        cnt += 1

print(n-cnt)

# 정렬 사용
import sys
input = sys.stdin.readline

n = int(input())
men = [list(map(int, input().split())) for _ in range(n)]
men.sort(reverse=True)

weight = 0
cnt = 0 
for x in men:
    if x[1] > weight:
        weight = x[1]
        cnt += 1

print(cnt)



# 창고정리
l = int(input())
box = list(map(int, input().split()))
m = int(input())
box.sort()

for _ in range(m):
    box[0] += 1
    box[-1] -= 1
    box.sort()

print(box[-1]-box[0])



# 침몰하는 타이타닉 (그리디)
from collections import deque

n, m = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort()
weight = deque(weight)

cnt = 0
while weight:
    min_w = weight.popleft()
    max_w = weight.pop()
    if min_w + max_w > m:
        weight.appendleft(min_w)
    cnt += 1

print(cnt)



# 증가수열 만들기 (그리디)
from collections import deque

def Left(n):
    stk.append(n)
    num.popleft()
    return 'L'

def Right(n):
    stk.append(n)
    num.pop()
    return 'R'


n = int(input())
num = deque(list(map(int, input().split())))
ans = ""
stk = []

while num:
    l = num[0]
    r = num[-1]

    if len(stk) == 0:
        if l <= r:
            ans += Left(l)
        else:
            ans += Right(r)
    else:
        if l > stk[-1] and r > stk[-1]:
            if l <= r:
                ans += Left(l)
            else:
                ans += Right(r)
        else:
            if l > stk[-1]: ans += Left(l)
            elif r > stk[-1] : ans += Right(r)
            else: break

print(len(stk))
print(ans)

n = int(input())
num = list(map(int, input().split()))

lt = 0
rt = n-1
last = 0
res = ''
tmp = []

while lt <= rt:
    if num[lt] > last:
        tmp.append((num[lt], 'L'))
    
    if num[rt] > last:
        tmp.append((num[rt], 'R'))

    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        res += tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1

    tmp.clear()

print(len(res))
print(res)



# 역수열 (그리디)
n = int(input())
num = list(map(int, input().split()))

chk = [0] * (n)
now = 1
for x in num:
    i = 0
    tmp = 0
    while True:
        if tmp == x and chk[i] == 0:
            chk[i] = now
            break
        
        if chk[i] == 0:
            tmp += 1
        i += 1
                
    now += 1

print(*chk)

n = int(input())
num = list(map(int, input().split()))
chk = [0] * (n)

for i in range(n):
    for j in range(n):
        if num[i] == 0 and chk[j] == 0:
            chk[j] = i+1
            break
        elif chk[j] == 0:
            num[i] -= 1

print(*chk)



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