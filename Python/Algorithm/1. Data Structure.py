# 자료구조

# 백준 10828. 스택
import sys
input = sys.stdin.readline

n = int(input())
stk = []
for _ in range(n):
    order = list(input().split())
    
    if order[0] == "push":
        stk.append(order[1])

    elif order[0] == "pop":
        if len(stk) > 0:
            print(stk.pop())
        else:
            print(-1)

    elif order[0] == "size":
        print(len(stk))

    elif order[0] == "empty":
        if len(stk) > 0:
            print(0)
        else:
            print(1)

    elif order[0] == "top":
        if len(stk) > 0:
            print(stk[-1])
        else:
            print(-1)



# 백준 10845. 큐
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
dq = deque()
for _ in range(n):
    order = input().split()

    if order[0] == "push":
        dq.append(order[1])

    elif order[0] == "pop":
        if dq:
            print(dq.popleft())
        else:
            print(-1)

    elif order[0] == "size":
        print(len(dq))

    elif order[0] == "empty":
        if dq:
            print(0)
        else:
            print(1)

    elif order[0] == "front":
        if dq:
            print(dq[0])
        else:
            print(-1)

    elif order[0] == "back":
        if dq:
            print(dq[-1])
        else:
            print(-1)



# 백준 10866. 덱
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
dq = deque()
for _ in range(n):
    order = input().split()

    if order[0] == "push_front":
        dq.appendleft(order[1])

    elif order[0] == "push_back":
        dq.append(order[1])

    elif order[0] == "pop_front":
        if dq:
            print(dq.popleft())
        else:
            print(-1)

    elif order[0] == "pop_back":
        if dq:
            print(dq.pop())
        else:
            print(-1)

    elif order[0] == "size":
        print(len(dq))

    elif order[0] == "empty":
        if dq:
            print(0)
        else:
            print(1)

    elif order[0] == "front":
        if dq:
            print(dq[0])
        else:
            print(-1)

    elif order[0] == "back":
        if dq:
            print(dq[-1])
        else:
            print(-1)



# 백준 1158. 요세푸스 문제
# 일일히 카운팅 -> 시간이 오래 걸림
from collections import deque

n, k = map(int, input().split())
dq = [i for i in range(1, n+1)]
dq = deque(dq)
res = []

cnt = 0
while dq:
    tmp = dq.popleft()
    cnt += 1

    if cnt == k:
        res.append(tmp)
        cnt = 0
    else:
        dq.append(tmp)

print('<' + ', '.join(map(str, res)) + '>')

# 인덱스를 카운팅해서 제거
n, k = map(int, input().split())
li = [i for i in range(1, n+1)]
res = []

p = 0
while len(res) != n:
    p = (p+k-1)%len(li)
    res.append(li.pop(p))

print('<' + ', '.join(map(str, res)) + '>')



# 백준 9093. 단어 뒤집기
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    word = list(map(str, input().split()))
    
    new = []
    for x in word:
        new.append(x[::-1])

    print(' '.join(new))

# 문자열 반대로 하는 방법
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    word = list(map(str, input().split()))

    print(' '.join(word[::-1])[::-1])



# 백준 9012. 괄호
# 자료구조
from collections import deque
import sys
iuput = sys.stdin.readline

n = int(input())
for _ in range(n):
    ps = list(map(str, input()))
    ps = deque(ps)
    stk = []

    if len(ps)%2 == 1:
        print("NO")
    else:
        while ps:
            tmp = ps.popleft()
            if tmp == "(":
                stk.append(tmp)
            else:
                if len(stk)> 0 and stk[-1] == "(":
                    stk.pop()
                else:
                    stk.append(1)
                    break
                    
        if len(stk) == 0:
            print("YES")
        else:
            print("NO")

# 구현 -> 조금 더 빠름
from collections import deque
import sys
iuput = sys.stdin.readline

n = int(input())
for _ in range(n):
    ps = input()
    while '()' in ps:
        ps = ps.replace('()', '')

    if ps:
        print("NO")
    else:
        print("YES")



# 백준 1966. 프린터 큐
from collections import deque
import sys
iuput = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    imp = list(map(int, input().split()))
    dq = [(idx, val) for idx, val in enumerate(imp)]
    dq = deque(dq)
    
    cnt = 0
    while dq:
        tmp = dq.popleft()
        
        if all(tmp[1] >= x[1] for x in dq):
            cnt += 1
            if tmp[0] == m:
                print(cnt)
                break
        else:
            dq.append(tmp)

# 기존 풀이
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



# 백준 11279. 최대 힙
import heapq
import sys
input = sys.stdin.readline

n = int(input())
num = []
for _ in range(n):
    x = int(input())

    if x == 0:
        if num:
            print(heapq.heappop(num)*-1)
        else:
            print(0)
    else:
        heapq.heappush(num, -x)



# 백준 11286. 절댓값 힙
import heapq
import sys
input = sys.stdin.readline

n = int(input())
num = []
for _ in range(n):
    x = int(input())

    if x == 0:
        if num:
            print(heapq.heappop(num)[1])
        else:
            print(0)
    else:
        heapq.heappush(num, (abs(x), x))



# 백준 2696. 중앙값 구하기
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m = int(input())

    num = []
    while True:
        num += list(map(int, input().split()))

        if len(num) == m:
            break
    
    print((m+1)//2)

    tmp = []
    cnt = 0
    for i in range(m):
        tmp.append(num[i])
        tmp.sort()

        if (i+1)%2 == 1:    # 홀수
            cnt += 1
            print(tmp[i//2], end=' ')

        if cnt == 10:
            print()
            cnt = 0
    
    print()
