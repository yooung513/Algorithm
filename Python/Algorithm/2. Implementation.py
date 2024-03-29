# 구현 알고리즘 (Implementation Algorithm)

# 백준 2438. 별 찍기 - 1 
n = int(input())
for i in range(1, n+1):
    print("*"*i)



# 백준 2439. 별 찍기 - 2
n = int(input())

for i in range(1, n+1):
    print(" "*(n-i) + "*"*i)



# 백준 2440. 별 찍기 - 3
n = int(input())

for i in range(n, 0, -1):
    print("*"*i)



# 백준 2441. 별 찍기 - 4
n = int(input())

for i in range(n, 0, -1):
    print(" "*(n-i) + "*"*i)



# 백준 2442. 별 찍기 - 5
n = int(input())

for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i-1))



# 백준 2443. 별 찍기 - 6
n = int(input())

for i in range(n, 0, -1):
    print(" "*(n-i) + "*"*(2*i-1))



# 백준 2444. 별 찍기 - 7
n = int(input())

for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i-1))

for j in range(n-1, 0, -1):
    print(" "*(n-j) + "*"*(2*j-1))


# 이전 풀이 
# 시간이 더 걸림 (메모리는 동일)
n = int(input())
s = e = ((2*n)-1)//2

for i in range((2*n)-1):
    for j in range((2*n)-1):
        if s > j:
            print(" ", end="")
        elif s<=j and j<=e:
            print("*", end="")
        else:
            break
    print()

    if i < ((2*n)-1)//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1



# 백준 5598. 카이사르 암호
caesar = str(input())

ori = ""
for i in caesar:
    n = ord(i) - 3
    if n < 65:
        ori += chr(n+26)
    else:
        ori += chr(n)
    
print(ori)



# 백준 2562. 최댓값
import sys
input = sys.stdin.readline

num = [int(input()) for _ in range(9)]
res = max(num)

for i, v in enumerate(num):
    if res == v:
        print(res)
        print(i+1)
        break

# 내장함수만 이용
# 시간이 조금 더 걸림
import sys
input = sys.stdin.readline

num = [int(input()) for _ in range(9)]
print(max(num))
print(num.index(max(num))+1)



# 백준 10872. 팩토리얼
# 재귀 사용
def Solve(n):
    if n <= 1:
        return 1
    else:
        return n*Solve(n-1)
    

n = int(input())

print(Solve(n))

# 단순 구현
n = int(input())

ans = 1
for i in range(1, n+1):
    ans *= i

print(ans)



# 백준 1037. 약수
n = int(input())
div = list(map(int, input().split()))
div.sort()

print(div[0]*div[-1])



# 백준 2576. 홀수
import sys
input = sys.stdin.readline

n_sum = 0
n_min = float('inf')
for _ in range(7):
    n = int(input())
    
    if n%2 == 1:
        n_sum += n

        if n_min > n:
            n_min = n

if n_sum == 0:
    print(-1)
else:
    print(n_sum)
    print(n_min)



# 백준 1546. 평균
n = int(input())
sco = list(map(int, input().split()))
m = max(sco)

res = 0
for s in sco:
    res += (s/m)*100

print(res/n)



# 백준 10818. 최소, 최대
# 내장함수 -> 가장 시간이 짧음
n = int(input())
num = list(map(int, input().split()))

print(min(num), max(num))

# 정렬 
n = int(input())
num = list(map(int, input().split()))
num.sort()

print(num[0], num[-1])



# 백준 10809. 알파벳 찾기
# index 함수 (더 빠름)
s = str(input())
alpha = [-1]*26

for i in range(97, 123):
    if chr(i) in s:
        alpha[i-97] = s.index(chr(i))

for alp in alpha:
    print(alp, end=' ')

# find 함수
a = input().lower()
b = list()

for i in range(97, 123) :
    if chr(i) in a :
        b.append(a.find(chr(i)))
    else : 
        b.append(-1)

for j in b :
    print(j, end = ' ')



# 백준 3460. 이진수
t = int(input())
for _ in range(t):
    n = int(input())

    p = 0
    while n > 0:
        if n%2 == 1:
            print(p, end=' ')

        n = n//2
        p += 1



# 백준 2869. 달팽이는 올라가고 싶다.
a, b, v = map(int, input().split())

if a >= v:
    print(1)
else:
    x = (v-b)/(a-b)
    if x == int(x):
        print(int(x))
    else:
        print(int(x)+1)



# 백준 24265. 알고리즘의 수행 시간 4
n = int(input())
print(((n-1)*n)//2)
print(2)



# 백준 24267. 알고리즘의 수행 시간 6
n = int(input())
print((n*(n-1)*(n-2))//6)
print(3)



# 이코테. 상하 좌우
# 나의 풀이
# 지도에서 여행자의 도착지점을 표시
# n : 공간의 크기           <= 100
# plan : 계획서 내용        <= 100

n = int(input())
plan = list(map(str, input().split()))
map = [[0]*(n+1) for _ in range(n+1)]

dx = [-1, 0, 1, 0]      # U R D L
dy = [0, 1, 0, -1]
now = [1, 1]
idx = 0 
for go in plan:
    if go == 'U':
        idx = 0
    elif go == 'R':
        idx = 1  
    elif go == 'D':
        idx = 2
    elif go == 'L':
        idx = 3
        
    if 0 < now[0]+dx[idx] <= n and 0 < now[1]+dy[idx] <= n:
        now[0] += dx[idx]
        now[1] += dy[idx]
        
print(*now)


# 답안 예시
# N을 입력 받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:                          # 이동 계획을 하나씩 확인
    for i in range(len(move_types)):        # 이동 후 좌표 구하기
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            
    if nx < 1 or ny < 1 or nx > n or ny > n:    # 공간을 벗어나는 경우 무시
        continue
    
    x, y = nx, ny                           # 이동 수행
    
print(x, y)
    
    
    
# 이코테. 왕실의 나이트
pos = input()
col = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

x = col.get(pos[0])
y = int(pos[1])
dx = [-2, -2, 1, -1, 2, 2, -1, 1]
dy = [1, -1, 2, 2, 1, -1, -2, -2]
cnt = 0
for i in range(8):
    if 0 < x+dx[i] <= 8 and 0 < y+dy[i] <= 8:
        cnt += 1
        
print(cnt)


# 답안 예시
# 현재 나이트의 위치 입력받기
input_data = input()

row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0 
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
        
print(result)



# 이코테. 럭키 스트레이트
n = list(str(input()))
left = 0
right = 0

for i in range(len(n)//2):
    left += int(n[i])
    right += int(n[-1-i])
    
if left == right:
    print("LUCKY")
else:
    print("READY")
    

# 답안 예시
n = input()
length = len(n)     # 점수값의 총 자릿수
summary = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(length // 2):
    summary += int(n[i])
    
# 오른쪽 부분의 자릿수 합 빼기
for i in range(length//2, length):
    summary -= int(n[i])
    
# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0:
    print("LUCKY")
else:
    print("READY")