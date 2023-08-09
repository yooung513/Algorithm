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


# 회의실 배정