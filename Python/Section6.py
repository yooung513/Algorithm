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



# 휴가
import sys
input = sys.stdin.readline

def Solve(idx, sum):
    global res

    if idx >= n:
        if sum > res:
            res = sum

    else:
        date = arr[idx][0]
        pay = arr[idx][1]

        # 상담을 하는 경우
        Solve(idx+date, sum+pay)

        #상담을 하지 않는 경우
        Solve(idx+1, sum)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = 0

Solve(0, 0)
print(res)

# 중간에 상담일이 휴가보다 긴 경우는 고려하지 않음으로 cut 할 수 있다.
# if idx+date <= n: 



# 양팔저울
import sys
input = sys.stdin.readline


def Solve(idx, sum):
    if idx == k:
        if 0 <= sum <= s:
            chk[sum] = 0
    else:
        # 저울의 왼쪽에 추를 올려놓음
        Solve(idx+1, sum+w[idx])

        # 저울의 오른쪽에 추를 올려놓음
        Solve(idx+1, sum-w[idx])

        # 저울에 추를 올려놓지 않음
        Solve(idx+1, sum)


k = int(input())
w = list(map(int, input().split()))
s = sum(w)
chk = [1]*(s+1)
chk[0] = 0

Solve(0, 0)
print(sum(chk))

# set을 활용하는 방법
import sys
input = sys.stdin.readline


def Solve(idx, sum):
    global res

    if idx == k:
        if 0 < sum <= s:    # 양수인 경우에만 값 입력
            res.add(sum)

    else:
        # 저울의 왼쪽에 추를 올려놓음
        Solve(idx+1, sum+w[idx])

        # 저울의 오른쪽에 추를 올려놓음
        Solve(idx+1, sum-w[idx])

        # 저울에 추를 올려놓지 않음
        Solve(idx+1, sum)


k = int(input())
w = list(map(int, input().split()))
s = sum(w)
res = set()

Solve(0, 0)
print(s-len(res))



# 동전 바꿔주기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


def Solve(idx, sum):
    global cnt
    if sum > t:
        return
    
    if idx == k:
        if sum == t:
            cnt += 1

    else:
        p = coin[idx][0]
        n = coin[idx][1]
        for i in range(n+1):
            Solve(idx+1, sum+(p*i))


t = int(input())    # 지폐의 금액
k = int(input())    # 동전의 가지수
coin = [list(map(int, input().split())) for _ in range(k)]  # 동전 (금액, 개수)
cnt = 0     # 교환 방법 카운트

Solve(0, 0)

print(cnt)