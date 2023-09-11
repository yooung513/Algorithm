# Section7. Dynamic Programming 동적계획법

# 네트워크 선 자르기
# Bottom-Up 방식
n = int(input())
res = [0]*(n+1)
res[1] = 1
res[2] = 2

for i in range(3, n+1):
    res[i] = res[i-1] + res[i-2]

print(res[n])

# Top-down 방식
def Solve(n):
    if n <= 2:
        return n
    else:
        return Solve(n-1) + Solve(n-2)

n = int(input())

print(Solve(n))



# 도전과제_계단 오르기
def Solve(n):
    if n <= 2:
        return n

    else:
        return Solve(n-1) + Solve(n-2)
    
n = int(input())

print(Solve(n))



# 도전과제_돌다리 건너기
n = int(input())
res = [0]*(n+1)
res[0] = 1
res[1] = 2

for i in range(2, n+1):
    res[i] = res[i-2] + res[i-1]

print(res[n])



# 최대 부분 증가수열
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
res = [0]*n

for i in range(n):
    tmp = []
    tmp.append(arr[i])
    
    for j in range(i+1, n):
        if arr[j] > tmp[-1]:
            tmp.append(arr[j])
    
    res[i] = len(tmp)

print(max(res))

# LIS 알고리즘
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)

lis = [0]*(n+1)
lis[1] = 1
res = 0

# 작은 값 부터 큰 값으로 풀어나가면서 메모하기
for i in range(2, n+1):
    max = 0     # 자신의 앞에서 기록된 만들 수 있는 최대 증가 수열
    
    # 이전 값 확인
    for j in range(i-1, 0, -1):
        if arr[i] > arr[j] and lis[j] > max:
            max = lis[j]
            
    lis[i] = max+1  # 자기 자신을 최종 수열에 더한 값

    # 최대 길이 수열 확인
    if lis[i] > res:
        res = lis[i]

print(res)