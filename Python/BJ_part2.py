# 알고리즘

# 백준 10814. 나이순 정렬
# 정렬
import sys
input = sys.stdin.readline

n = int(input())
per = []

for i in range(1, n+1):
    age, name = input().split()
    age = int(age)
    per.append((age, i, name))

per.sort()
for a, i, n in per:
    print(a, n)

# 나이순으로만 정렬 -> 이름순 자동 정렬
n = int(input())
arr = []

for _ in range(n):
    data = input().split()
    arr.append(int(data[0]), data[1])

arr = sorted(arr, key= lambda x: x[0])

for i in arr:
    print(i[0], i[1])



# 수 정렬하기 3
# 정렬 -> 카운팅 정렬 (계수 정렬 알고리즘)

# 힙정렬 풀이 (다영) -> 메모리 초과
import sys
input = sys.stdin.readline
import heapq as hq

n = int(input())
num = []
for _ in range(n):
    x = int(input())
    hq.heappush(num, x)

for _ in range(n):
    hq.heappop(num)


# 계수 정렬 (Counting Sort)
import sys
input = sys.stdin.readline

n = int(input())
num = [0]*10001

for _ in range(n):
    data = int(input())
    num[data] += 1

for i in range(10001):
    if num[i] != 0:
        for j in range(num[i]):
            print(i)



# 백준 11726. 2xn 타일링
# 동적 계획법
def cnt(n):
    dp = [0] * (1001)
    dp[1], dp[2] = 1, 2

    if n > 2:
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]

    return dp[n]

n = int(input())
print(cnt(n) % 10007)



# 백준 9461. 파도반 수열
def P(n):
    res = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    if n > 10:
        tmp = [0]*(n-10)
        res = res+tmp
        
        for i in range(11, n+1):
            res[i] = res[i-1] + res[i-5]
    
    return res[n]

t = int(input())
for _ in range(t):
    n = int(input())
    print(P(n))

# 점화식 : dp[i] = dp[i-3] + dp[i-2]
dp = [0]*101
dp[1], dp[2], dp[3] = 1, 1, 1

for i in range(3, 101):
    dp[i] = dp[i-3] + dp[i-2]

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])



# 백준 2747. 피보나치 수
# 재귀함수

# 풀이 -> 시간초과
def fibo(x):
    res = [0]*(46)
    res[1] = 1

    if x > 1:
        res[x] = fibo(x-1) + fibo(x-2)
    
    return res[x]
        
n = int(input())
print(fibo(n))

# 풀이
n = int(input())
res = [0]*(46)
res[1] = 1

if n < 2:
    print(n)
else:
    for i in range(2, n+1):
        res[i] = res[i-1] + res[i-2]
    print(res[n])



# 백준 1074. Z
# 재귀함수
# 시간 초과남 -> 해결할 것
def solve(n, x, y):
    global result
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        
        result += 1
        if x == X and y+1 == Y:
            print(result)
            return

        result += 1
        if x+1 == X and y == Y:
            print(result)
            return

        result += 1
        if x+1 == X and y+1 == Y:
            print(result)
            return
        
        result += 1
        return
    
    solve(n/2, x, y)
    solve(n/2, x, y+n/2)
    solve(n/2, x+n/2, y)
    solve(n/2, x+n/2, y+n/2)



result = 0
N, X, Y = map(int, input().split())
solve(2**N, 0, 0)



# 백준 1543. 문서 검색
# 탐색
org = input()
word = input()
cnt = 0

while True:
    if word not in org:
        break
    else:
        org = org.replace(word, '*', 1)
        cnt += 1

print(cnt)



# 백준 1568. 새
# 팀섹
n = int(input())

time = 0
k = 1
now = n
while True:
    if now == 0:
        break

    if now < k:
        k = 1
    else:
        now -= k
        time += 1
        k += 1
        
print(time)



# 백준 1302. 베스트 셀러
# 탐색
import sys
input = sys.stdin.readline

n = int(input())
book = dict()

for _ in range(n):
    name = input().strip()
    
    if name in book:
        book[name] += 1
    else:
        book[name] = 1

cnt = max(book.values())
res = []
for key, val in book.items():
    if val == cnt:
        res.append(key)

res.sort()
print(res[0])



# 백준 1668. 트로피 진열
# 탐색
import sys
input = sys.stdin.readline

n = int(input())
real = []
left = 0
left_cnt = 0
for i in range(n):
    now = int(input())
    real.append(now)

    if left < now:
        left = now
        left_cnt += 1

real.reverse()
right = 0
right_cnt = 0
for x in real:
    if right < x:
        right = x
        right_cnt += 1

    if right == left:
        break

print(left_cnt)
print(right_cnt)



# 백준 2751. 수 정렬하기 2
# 정렬
import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    m = int(input())
    heapq.heappush(arr, m)

for _ in range(n):
    print(heapq.heappop(arr))



# 백준 11004. K번째 수
# 정렬
n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
print(arr[k-1])



# 백준 7490. 0만들기
# 재귀호출
def Solve(idx):
    tmp.append(str(idx))

    if idx == n:
        res = ''.join(tmp)
        ans = res.replace(' ', '')
        if eval(ans) == 0:
            print(res)
        tmp.pop()
            
    else:
        for i in range(3):
            tmp.append(opr[i])
            Solve(idx+1)
            tmp.pop()
        tmp.pop()


t = int(input())
opr = [' ', '+', '-']

for _ in range(t):
    n = int(input())
    tmp = []
    Solve(1)
    print()



# 성지키기