# Section 2. 탐색 & 시뮬레이션

# 회문 문자열 검사
# 나의 풀이 -> 파이썬 기능 활용
n = int(input())
for _ in range(n):
    word = input().lower()
    if word == word[::-1]:
        print("YES")
    else:
        print("NO")

#직접 구현문
n = int(input())
for _ in range(n):
    word = input().lower()
    for i in range(len(word)//2):
        if word[i] != word[-1-i]:
            print("NO")
            break
    else:
        print("YES")



# 숫자만 추출
# 나의 풀이
# isdecimal() : 숫자(0~9), 유니코드
# isdigit()   : 숫자(0~9), 유니코드, 지수
# isnumeric() : 숫자(0~9), 유니코드, 지수, 분수
ss = input()

n = ""
for s in ss:
    if s.isnumeric() :
        n += s
n = int(n)

cnt = 0
for i in range(1, int(n**0.5)+1) : 
    if n%i == 0:
        if i**2 == n:
            cnt += 1
        else:
            cnt += 2
        
print(n)
print(cnt)

# 직접 구현문 
ss = input()

n = 0
for s in ss:
    if s.isdigit():
        n = 10*n + int(s)
print(n)

cnt = 0
for i in range(1, int(n**0.5)+1):
    if n%i == 0:
        if i**2 == n:
            cnt += 1
        else:
            cnt += 2
print(cnt)



# 카드 역배치
# 출력 시 제일 처음 원소를 추출/제거 해서 출력하기 가능 (pop(0))
card = [i for i in range(21)]

for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        card[s+i], card[e-i] = card[e-i], card[s+i]

for j in range(1, 21):
    print(card[j], end=" ")


# 두 리스트 합치기
# 나의 풀이 -> 직접 구현문으로 풀이
# 파이썬의 경우 리스트끼리 합치기 가능
# 다만 sort의 시간복잡도는 nlogn으로 
# 처음 주어진 리스트가 정렬이 되어있는 경우는 직접 구현문이 효율적
ns = int(input())
n = list(map(int, input().split()))

ms = int(input())
m = list(map(int, input().split()))

res = []
np, mp = 0, 0
while np < ns and mp < ms:
    if n[np] <= m[mp]:
        res.append(n[np])
        np += 1
    else:
        res.append(m[mp])
        mp += 1

if np < ns:
    res += n[np:]
elif mp < ms:
    res += m[mp:]

for x in res:
    print(x, end=" ")



# 수들의 합 (**)
# 나의 풀이
n, m = map(int, input().split())
a = list(map(int, input().split()))

s, e, cnt = 0, 0, 0 
while s <= e and e < n:
    chk = 0
    for i in range(s, e+1):
        chk += a[i]

    if chk == m:
        cnt += 1
        s += 1
        e += 1
    elif chk < m :
        e += 1
    else:
        s += 1

print(cnt)

# 강의 자료
# 인덱스 위치 표시를 활용
n, m = map(int, input().split())
a = list(map(int, input().split()))

l, r = 0, 1
tot, cnt = a[l], 0
while True:
    if tot < m:
        if r < n:
            tot += a[r]
            r += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[l]
        l += 1
    else:
        tot -= a[l]
        l += 1
         
print(cnt)

# 인덱스를 활용하는 방법 우선 생각하기!



# 격자판 최대합
# 나의 풀이 -> max 함수 사용
# 변수를 최대값으로 초기화 하는 방법 존재
n = int(input())
a = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    a.append(tmp)

mx1 = 0
for i in range(n):
    tmpr, tmpc = 0, 0
    for j in range(n):
        tmpr += a[i][j]
        tmpc += a[j][i]
    mx1 = max(mx1, tmpr, tmpc)

mx2, tmpl, tmpr = 0, 0, 0
for x in range(n):
    tmpl += a[x][x]
    tmpr += a[x][n-1-x]
    mx2 = max(tmpl, tmpr)

print(max(mx1, mx2))

# 격자판 값 입력 방법
a = [list(map(int, input().split())) for _ in range(n)]



# 사과나무 (다이아몬드)
# 나의 풀이 
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

s, e = n//2, n//2
res = 0
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(res)



# 곶감 (모래시계)
# 오른쪽으로 회전하는 경우 앞으로 insert 하는 것 잘 알아두기
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
for _ in range(m):
    x, y, z = map(int, input().split())
    if y == 0:
        for _ in range(z):
            a[x-1].append(a[x-1].pop(0))
    else:
        for _ in range(z):
            a[x-1].insert(0, a[x-1].pop())

s, e, res = 0, n-1, 0
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(res)



# 봉우리
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n)
a.append([0]*n)
for i in range(len(a)):
    a[i].insert(0, 0)
    a[i].append(0)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
for x in range(1, n+1):
    for y in range(1, n+1):
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if a[x][y] <= a[xx][yy]:
                break
        else:
            cnt += 1

print(cnt)

# 강의 -> 한 번에 상하좌우 변수 체크하기 -> all 사용
for i in range(1, n+1):
    for j in range(1, n+1):
        if all( a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1



# 스도쿠 검사 (4중 for문)
a = [list(map(int, input().split())) for _ in range(9)]
chkr = [0]*10
chkc = [0]*10
for i in range(9):
    for j in range(9):
        chkr[a[i][j]] = 1
        chkc[a[j][i]] = 1
    if sum(chkr) != 9 or sum(chkc) != 9:
        print("NO")
        break
    else:
        chkr = [0]*10
        chkc = [0]*10

if sum(chkr) == 9 and sum(chkc) == 9:
    chk = [0]*10
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            for i in range(3):
                for j in range(3):
                    chk[a[i+x][j+y]] = 1
        if sum(chk) != 9:
            print("NO")
            break
        else:
            chk = [0]*10
    else:
        print("YES")

# 함수로 검사한 후 return 값 활용하기
def check(a):
    # 행-열 검사
    for i in range(9):
        chk1 = [0]*10   # 초기화
        chk2 = [0]*10 
        for j in range(9):
            chk1[a[i][j]] = 1
            chk2[a[i][j]] = 1
        if sum(chk1) != 9 or sum(chk2) != 9:
            return False #break로 함수 종료 역할까지 가능

    # 그룹검사
    for i in range(3):
        for j in range(3):
            chk3 = [0]*10
            for k in range(3):
                for s in range(3):
                    chk3[a[i*3+k][j*3+s]] = 1
            if sum(chk3) != 9:
                return False
    return True

a = [list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")


