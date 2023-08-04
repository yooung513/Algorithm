# 자료구조

# 백준 2920. 음계
chk = list(map(int, input().split()))
ans = ""

for i in range(7):
    tmp = chk[i+1]-chk[i]
    if tmp == 1:
        ans = "ascending"
    elif tmp == -1:
        ans = "descending"
    else:
        print("mixed")
        break
else:
    print(ans)



# 백준 2798. 블랙잭
n, m = map(int, input().split())
card = list(map(int, input().split()))

res = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            tmp = card[i]+card[j]+card[k]
            if tmp <= m:
                res = max(res, tmp)

print(res)



# 백준 1874. 스택수열
# python의 경우 시간초과
n = int(input())
num = [i for i in range(1, n+1)]
ans = [int(input()) for _ in range(n)]
stk = []
res = []
ap = 0
flag = 'y'

while ap < n:
    if ans[ap] in stk:
        if ans[ap] == stk[-1]:
            stk.pop()
            res.append('-')
            ap += 1
        else:
            flag = 'n'
            break
    else:
        stk.append(num.pop(0))
        res.append('+')

if flag == 'y':
    for x in res:
        print(x)
else:
    print("NO")

# 풀이
# 파이썬에서도 사용 가능!! -> 시간 복잡도가 좀 더 유연함
# ! 스택의 최상위 원소 top()보다 작은 값을 꺼내는 것은 불가능 -> NO
n = int(input())

cnt = 1
stk = []
res = []

for i in range(1, n+1):     # 데이터 개수만큼 반복
    data = int(input())
    while cnt <= data:      # 입력 받은 데이터에 도달할 때 까지 삽입
        stk.append(cnt)
        cnt += 1
        res.append('+')
    if stk[-1] == data:     # 스택의 최상위 원소가 데이터와 같을 때 출력
        stk.pop()
        res.append('-')
    else:
        print('NO')
        exit(0)             # 코드 종료 (프로그램 실행 종료)

print('\n'.join(res))

# 유사 방법
import sys
input = sys.stdin.readline

n = int(input())    
stack = []      # 스택 초기화
answer = []     # 최종 정답
current = 1     # 현재 삽입할 수 (조건에 의해 오름차순으로 증가함을 확인)

for _ in range(n):
    x = int(input())

    # top보다 x가 더 큰 경우, 스택에 삽입
    while stack or stack[-1] < x:
        stack.append(current)
        current += 1
        answer.append('+')

    # top과 x가 같다면, 스택에서 제거
    if stack[-1] == x:
        stack.pop()
        answer.append('-')

    # top보다 x가 작은 경우, 불가능
    else:
        answer = ['NO']
        break

for x in answer:
    print(x)



# 백준 1966. 프린터 큐
from collections import deque

t = int(input())
res = []

for _ in range(t):
    n, m = map(int, input().split())
    imp = list(map(int, input().split()))
    
    dq = deque()
    for idx, val in enumerate(imp):
        dq.append([idx, val])
    
    imp.sort(reverse=True)
    cnt = 0
    while dq:
        tmp = dq.popleft()
        idx = tmp[0]
        val = tmp[1]
        if val == imp[cnt]:
            cnt += 1
            if idx == m:
                res.append(cnt)
                break
        else:
            dq.append(tmp)    

for x in res:
    print(x)

# 풀이
test_case = int(input())

for _ in range(test_case):
    n, m = list(map(int, input().split()))
    queue = list(map(int, input().split()))
    queue = [(i, idx) for idx, i in enumerate(queue)]

    count = 0
    while True:
        if queue[0][0] == max(queue, key= lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))



# 백준 5397. 키로거
# 나의 풀이 -> 시뮬레이션 방식 불가 (테스트 길이 1,000,000)
# 런타임 에러 발생
t = int(input())
res = []

cs = 0
pw = []
for _ in range(t):
    l = list(input())
    for x in l:
        if x == '<':
            cs -= 1
            if cs < 0:
                cs = 0
        elif x == '>':
            cs += 1
            if len(pw) == 0:
                cs = 0
            elif len(pw) < cs:
                cs = len(pw)
        elif x == '-':
            if pw and cs > 0:
                del pw[cs-1]
                cs -= 1
        else:
            pw.insert(cs, x)
            cs += 1
    res.append(''.join(pw))
    pw = []

for x in res:
    print(x)


# 풀이
# 커서를 중심으로 왼쪽/오른쪽에 스택 사용 (이때 오른쪽 스택의 경우 반대로 추출)
t = int(input())
res = []
for _ in range(t):
    tmp = list(input())
    l = []
    r = []
    for x in tmp:
        if x == '<':
            if l: 
                r.append(l.pop())
        elif x == '>':
            if r:
                l.append(r.pop())
        elif x == '-':
            if l:
                l.pop()
        else:
            l.append(x)
    res.append(''.join(l + r[::-1]))

for x in res:
    print(x)

# 스택 연결 방법
l.extend(reversed(r))



# 백준 1920. 수찾기
n = int(input())
num = list(map(int, input().split()))
m = int(input())
chk = list(map(int, input().split()))
res = []
num = set(num)

for x in chk:
    if x in num:
        res.append(1)
    else:
        res.append(0)

for x in res:
    print(x)

# 풀이
# 처음부터 셋으로 받음 -> 순서에 영향을 받지 않음
n = int(input())
arr = set(map(int, input().split()))
m = int(input())
x = list(map(int, input()))

for i in x:
    if i not in arr:
        print('0')
    else:
        print('1')



# 백준 4195. 친구 네트워크
# 나의 풀이 -> 못품
t = int(input())

for _ in range(t):
    f = int(input())
    frd = []
    chk = set()

    for i in range(f):
        x, y = map(str, input().split())
        frd.append({x, y})
        n = 0
        while n <= i:
            tmp = frd[n]
            if len(chk & tmp) == 0:
                chk = tmp | chk
                print(2)
                break
            else:
                chk = tmp | chk
                n += 1
        print(len(chk))

# 강의
# Union-Find (합집합 찾기) 사용
def find (x):          # 최상단 부모노드 찾음
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]
    
def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:          # 연결되어 있지 않음
        parent[y] = x   # 왼쪽 값을 부모로
        number[x] += number[y]


t = int(input())

for _ in range(t):
    parent = dict()
    number = dict()

    f = int(input())
    for _ in range(f):
        x, y = input().split()

        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        
        union(x, y)     # 네트워크 합집합

        print(number[find(x)])  # 값 찾아서 네트워크 크기 출력



# 백준 10838. 스택
# 빠른 입력 함수 사용 ***
import sys
input = sys.stdin.readline      # 빠른 입력 함수 사용

n = int(input())
stk = []

for _ in range(n):
    order = input().strip()
    if order == "pop":
        if stk:
            print(stk.pop())
        else:
            print(-1)
    elif order == "size":
        print(len(stk))
    elif order == "empty":
        if stk:
            print(0)
        else:
            print(1)
    elif order == "top":
        if stk:
            print(stk[-1])
        else:
            print(-1)
    else:
        num = list(order.split())
        x = int(num[1])
        stk.append(x)

# * sys.stdin.readline -> 입력 받은 문자 끝에 개행 문자 표함
#   따라서 strip()으로 개행문자 제거, split()써서 묶은 후 cmd[0] 값과 비교하기



# 백준 10773. 제로
# 빠른 입력 함수 사용 가능
import sys
input = sys.stdin.readline

x = int(input())
# 정수의 경우 그대로 사용

k = int(input())
stk = []

for _ in range(k):
    x = int(input())
    if x == 0:
        stk.pop()
    else:
        stk.append(x)

print(sum(stk))



# 백준 17298. 오큰수
# 1차 -> 시간초과
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = deque(a)
res = []

for i in range(n):
    tmp = b.popleft()
    for j in range(i+1, n):
        if tmp < a[j]:
            res.append(a[j])
            break
    else:
        res.append(-1)

print(*res)


# 풀이
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
nge = [-1] * n
stk = []

for i in range(n):
    tmp = a[i]

    # 스택의 top이 tmp보다 작거나 같음 / 스택이 비어있음 -> 원소 추가
    if len(stk) == 0 or stk[-1][1] >= tmp:
        stk.append((i, tmp))
    
    # 스택의 상단 값보다 큼 -> 오큰수
    else:
        while stk:
            idx, val = stk.pop()
            if val >= tmp:      # 크거나 같은 이전 원소를 만났다면 다시 삽입
                stk.append((idx, val))
                break
            else:               # 오큰수 기록
                nge[idx] = tmp  
        stk.append((i, tmp))

print(*nge)



# 백준 1021. 회전하는 큐
from collections import deque

n, m = map(int, input().split())
num = [i for i in range(1, n+1)]
rmv = list(map(int, input().split()))
num = deque(num)

res = 0
for i in range(m):
    left = num.index(rmv[i])
    right = len(num) - left

    if left <= right:
        for _ in range(left):
            num.append(num.popleft())
        res += left

    elif left > right:
        for _ in range(right):
            num.insert(0, num.pop())
        res += right

    num.popleft()

print(res)



# 백준 11866. 요세푸스 문제 0
from collections import deque

n, k = map(int, input().split())
a = deque(i for i in range(1, n+1))
res = []

cnt = 0
while a:
    now = a.popleft()
    cnt += 1
    if cnt == k:
        res.append(now)
        cnt = 0
    else:
        a.append(now)

print('<' + ', '.join(map(str, res)) + '>')



# 백준 2346. 풍선 터뜨리기
# 구현 제대로 하기!!
from collections import deque

n = int(input())
bal = deque((idx+1, val) for idx, val in enumerate(map(int, input().split())))
res = []

now = bal.popleft()
idx = now[0]
val = now[1]

res.append(idx)

for i in range(n-1):
    if val > 0:
        for _ in range(val-1):
            bal.append(bal.popleft())
    else:
        for _ in range(-val):
            bal.appendleft(bal.pop())
    
    now = bal.popleft()
    idx = now[0]
    val = now[1]
    res.append(idx)

print(*res)



# 백준 13335. 트럭
from collections import deque

n, w, l = map(int, input().split())
tr = deque(map(int, input().split()))
can = [0] * w
can = deque(can)

time = 0
while tr:
    for i in range(w):
        time += 1
        can.popleft()
        if len(tr) != 0:
            now = tr.popleft()
            can.append(now)
        else:
            can.append(0)

        if sum(can) > l:
            tr.appendleft(can.pop())
            can.append(0)
            break

while sum(can) > 0:
    time += 1
    can.popleft()

print(time)



# 백준 2953. 나는 요리사다
sco = [0]*5

for i in range(5):
    tmp = list(map(int, input().split()))
    sco[i] = sum(tmp)

res = max(sco)
print(sco.index(res)+1, res)



# 백준 11286. 절댓값 힙
import sys
import heapq as hq

input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    x = int(input())

    if x == 0:
        if len(arr) == 0:
            print(0)
        else:
            y = hq.heappop(arr)
            print(y[1])

    else:
        hq.heappush(arr, (abs(x), x))



####



# 백준 20040. 사이클 게임
import sys
input = sys.stdin.readline

def find(x):
    if arr[x] == x:
        return x
    else:
        p = find(arr[x])
        arr[x] = p
        return arr[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x != y:
        arr[y] = x


n, m = map(int, input().split())
arr = [i for i in range(n)]
vis = set()
fir = 0

for i in range(m):
    x, y = map(int, input().split())

    if x > y:
        x, y = y, x
    
    if (x, y) not in vis:
        vis.add((x, y))

        if find(x) == find(y) :
            fir = i+1
            break
        else:
            union(x, y)
    
print(fir)



# 백준 11724. 연결 요소의 개수
import sys
input = sys.stdin.readline

def find(x):
    if x == res[x]:
        return x
    else:
        p = find(res[x])
        res[x] = p
        return res[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        res[x] = y
    else:
        res[y] = x


n, m = map(int, input().split())
res = [i for i in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    
    if x > y:
        x, y = y, x

    union(x, y)

ans = set()
for i in range(1, n+1):
    ans.add(find(res[i]))

print(len(ans))



# 백준 1233. 주사위
a, b, c = map(int, input().split())
res = dict()

for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            s = i+j+k
            if s in res.keys():
                res[s] += 1
            else:
                res[s] = 1

num = 0
ans = 0
for s, n in res.items():
    if n > num:
        num = n
        ans = s

print(ans)



# 백준 1374. 강의실
# 메모리 초과
import sys
input = sys.stdin.readline

n = int(input())
rec = dict()

for _ in range(n):
    num, std, end = map(int, input().split())

    for i in range(std, end):
        if i in rec.keys():
            rec[i] += 1
        else:
            rec[i] = 1

print(max(rec.values()))



# 백준 1374. 강의실
import heapq as hq

import sys
input = sys.stdin.readline

n = int(input())
lec = []
for _ in range(n):
    num, str, end= map(int, input().split())
    hq.heappush(lec, (str, end))

room = []
e = hq.heappop(lec)[1]
hq.heappush(room, e)
for _ in range(n-1):
    new_str, new_end = hq.heappop(lec)
    org = hq.heappop(room)

    if new_str < org:       # 겹치는 경우
        hq.heappush(room, org)

    hq.heappush(room, new_end)

print(len(room))