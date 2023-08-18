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