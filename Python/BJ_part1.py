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



# 블랙잭
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



# 스택수열
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



# 프린터 큐
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



# 키로거
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