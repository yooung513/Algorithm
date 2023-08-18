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
