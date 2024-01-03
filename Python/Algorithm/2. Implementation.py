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
