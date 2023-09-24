# 투포인터 (Two Pointer)

# 백준 2230. 수 고르기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()

s, e = 0, 1
res = float('inf')
while s <= e and e < n:
    tmp = a[e]-a[s]
    
    if tmp < m:
        e += 1
    else:
        res = min(res, tmp)
        s += 1

        if tmp == m:
            break
        
print(res)