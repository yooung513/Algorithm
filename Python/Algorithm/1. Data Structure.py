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