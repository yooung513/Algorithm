# 탐색

# 백준 1236. 성 지키기
import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
castle = [list(input().strip()) for _ in range(n)]

row_need = 0
for i in range(n):
    for j in range(m):
        if castle[i][j]=='X':
            break
    else:
        row_need += 1

col_need = 0
for j in range(m):
    for i in range(n):
        if castle[i][j] == 'X':
            break
    else:
        col_need += 1

print(max(row_need, col_need))



# 백준 2110. 공유기 설치
import sys 
input = sys.stdin.readline

# 거리에 따른 공유기의 개수를 세는 함수
def Count(len):
    end = house[0]    # 제일 처음 집에 공유기 설치
    cnt = 1
    for i in range(1, n):
        if house[i]-end >= len:
            cnt += 1
            end = house[i]

    return cnt


n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

s, e = 1, house[n-1]
res = 0
while s <= e:
    mid = (s+e)//2

    if Count(mid) >= c:
        res = mid
        s = mid+1
    else:
        e = mid-1

print(res)



# 백준 1927. 최소 힙
import sys 
import heapq

n = int(input())
arr = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(arr, x)
    else:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr))



# 백준 1920. 수찾기
import sys
import time
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))   #주어진 수
m = int(input())
chk = list(map(int, input().split()))   #확인할 수 

arr.sort()

for c in chk:
    s, e = 0, n-1
    ans = 0
    while s <= e:
        mid = (s+e)//2
        if arr[mid] == c:   # 존재 하는 경우
            ans = 1
            break
        elif arr[mid] < c:  # 주어진 수보다 작은 경우
            s = mid+1
        elif arr[mid] > c:  # 주어진 수보다 큰 경우
            e = mid-1
    
    print(ans)

# 내장함수 사용
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



# 백준 10816. 숫자 카드 2
# 카운터
from collections import Counter
import sys
input = sys.stdin.readline


n = int(input())
num = list(map(int, input().split()))   #숫자 카드의 수
m = int(input())
chk = list(map(int, input().split()))   #확인할 수
res = []    #답

count = Counter(num)
num = set(num)

for c in chk:
    if c not in num:
        res.append(0)
    else:
        res.append(count[c])

print(' '.join(map(str, res)))

# 배열
from collections import Counter
import sys
input = sys.stdin.readline


n = int(input())
num = list(map(int, input().split()))
m = int(input())
chk = list(map(int, input().split()))
res = [0] * 20000001

for i in num:
    res[i+10000000] += 1

for j in chk:
    print(res[j+10000000], end=' ')

# 이분탐색 -> 시간초과
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))   #숫자 카드의 수
m = int(input())
chk = list(map(int, input().split()))   #확인할 수
res = []    #답

num.sort()

for c in chk:
    s, e = 0, n-1
    cnt = 0
    while s <= e:
        mid = (s+e)//2
        
        #카드에 수가 존재하는 경우
        if num[mid] == c:
            cnt += 1
            
            #앞-뒤로 같은 수가 있는 경우 체크
            #앞의 수 체크
            for i in range(mid-1, -1, -1):
                if num[i] == c:
                    cnt += 1
                else:
                    break
                
            #뒤의 수 체크
            for j in range(mid+1, n):
                if num[j] == c:
                    cnt += 1
                else:
                    break
            
            #이분탐색 종료 (같은 수의 값 다 찾음)
            break
        
        # 주어진 수보다 작은 경우
        elif num[mid] < c:
            s = mid+1
        
        # 주어진 수보다 큰 경우
        else:
            e = mid-1
            
    
    res.append(str(cnt))

print(' '.join(res))



# 백준 10815. 숫자 카드
# 백준 1920. 수 찾기와 유사
# 이분탐색
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
m = int(input())
chk = list(map(int, input().split()))

num.sort()
for c in chk:
    s, e = 0, n-1
    ans = 0
    while s <= e:
        mid = (s+e)//2
        if num[mid] == c:
            ans = 1
            break
        
        elif num[mid] < c:
            s = mid+1

        else:
            e = mid -1
    
    print(ans, end=' ')

# 내장함수 set 사용
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
m = int(input())
chk = list(map(int, input().split()))

num = set(num)
for c in chk:
    if c in num:
        print(1, end=' ')
    else:
        print(0, end=' ')



# 백준 1822. 차집합
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = list(set(a)-set(b))
res.sort()

print(len(res))
if len(res) != 0:
    print(' '.join(map(str, res)))

# 이분탐색
import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = []

b.sort()
for x in a:
    tmp = x
    s, e = 0, m-1
    while s <= e:
        mid = (s+e)//2

        if b[mid] == x:
            tmp = 0
            break

        elif b[mid] < x:
            s = mid+1

        else:
            e = mid-1

    if tmp != 0:
        res.append(tmp)
        
print(len(res))
if len(res) > 0:
    print(*sorted(res))



# 백준 7453. 합이 0인 네 정수
# 시간초과
import sys
input = sys.stdin.readline


n = int(input())
arrA = [] 
arrB = []
arrC = []
arrD = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    arrA.append(a)
    arrB.append(b)
    arrC.append(c)
    arrD.append(d)


# A+B => arr1, C+D => arr2
arr1, arr2 = [], []
for a in arrA:
    for b in arrB:
        arr1.append(a+b)

for c in arrC:
    for d in arrD:
        arr2.append(c+d)


# 두 개의 배열의 값들을 더했을 때 0이 되는 값 찾기
arr2.sort()
cnt = 0

for x in arr1:
    s, e = 0, (n*n)-1
    while s <= e:
        mid = (s+e)//2

        if arr2[mid]+x == 0:
            cnt += 1
            # 중복 값이 있는 경우
            tmp1 = mid
            # 현재 인덱스 앞에 중복값이 존재하는 경우
            while True:
                tmp1 -= 1
                if arr2[tmp1]+x == 0:
                    cnt += 1
                else:
                    break
            
            tmp2 = mid
            # 현재 인덱스 뒤에 중복값이 존재하는 경우
            while True:
                tmp2 += 1
                if arr2[tmp2]+x == 0:
                    cnt += 1
                else:
                    break
            break

        elif arr2[mid]+x < 0:
            s = mid+1

        else:
            e = mid-1

print(cnt)

# dict 사용 
# 시간초과 (메모리 초과로 예상)
import sys
input = sys.stdin.readline


n = int(input())
arrAB = []
arrCD = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    arrAB.append((a, b))
    arrCD.append((c, d))

# 각각의 A, B의 값 합과 C, D값의 합을 구해서 dict에 입력
dicAB = dict()
dicCD = dict()
for i in range(n):
    for j in range(n):
        x = arrAB[i][0] + arrAB[j][1]
        y = arrCD[i][0] + arrCD[j][1]

        if x not in dicAB :
            dicAB[x] = 1
        else:
            dicAB[x] += 1

        if y not in dicCD:
            dicCD[y] = 1
        else:
            dicCD[y] += 1

cnt = 0
for k, v in dicAB.items():
    if -1 * k in dicCD.keys():
        cnt += v

print(cnt)

# 풀이
import sys
input = sys.stdin.readline


n = int(input())
arrA = []
arrB = []
arrC = []
arrD = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    arrA.append(a)
    arrB.append(b)
    arrC.append(c)
    arrD.append(d)

# 각각의 A, B의 값 합과 C, D값의 합을 구해서 dict에 입력
dicAB = dict()
for a in arrA:
    for b in arrB:
        x = a+b
        if x not in dicAB:
            dicAB[x] = 1
        else:
            dicAB[x] += 1

cnt = 0
for c in arrC:
    for d in arrD:
        y = (c+d) * -1
        if y in dicAB.keys():
            cnt += dicAB[y]

print(cnt)