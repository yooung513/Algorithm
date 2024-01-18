# 이코테 1-그리디. 큰 수의 법칙
# 기존 풀이 - 반복문 사용
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

cnt = 0
ans = 0
while m > 0:
    if m >= k:
        ans += arr[0]*k
        ans += arr[1]
        m -= (k+1)
    else:
        ans += arr[0]*m
        break
    
print(ans)

# 수학적 구현
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
x = arr[0]  # 가장 큰 값
y = arr[1]  # 두 번째로 큰 값

ans = ((k*x + y) * (m//(k+1))) + (x*(m % (k+1)))
print(ans)



# 이코테. 숫자 카드 게임
import sys

n, m = map(int, input().split())

res = float('-INF')
for _ in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    
    if res < min(arr):
        res = min(arr)

print(res)



# 이코테. 1이 될 때 까지
n, k = map(int, input().split())

cnt = 0
while n != 1:
    if n % k == 0:
        n //= k
    else:
        n -= 1

    cnt += 1

print(cnt)



# 이코테. 모험가 길드
# 나의 풀이
n = int(input())
x = list(map(int, input().split()))

x.sort()
tmp = list()
cnt = 0
for i in x:
    tmp.append(i)
    
    if len(tmp) == tmp[-1]:
       cnt += 1
       tmp.clear()
       
print(cnt) 

# 답안 예시
n = int(input())
x = list(map(int, input().split()))
x.sort()

res = 0         # 총 그룹의 수
cnt = 0         # 현재 그룹에 포함된 모험가의 수

for i in x:     # 공포도가 낮은 사람부터 하나씩 확인하기 
    cnt += 1    # 현재 그룹에 모험가를 포함시키기
    
    if cnt >= i:    # 현재 그룹에 포함한 모험가의 수가 현재 공포도 이상이라면, 그룹을 결성한다.
        res += 1    # 총 그룹의 수 증가
        cnt = 0     # 현재 그룹에 포함된 모험가의 수 초기화
        
print(res)



# 이코테. 곱하기 혹은 더하기
# 나의 풀이
s = list(map(str, input()))

ans = 0
for x in s:
    tmp = int(x)
    
    if ans <= 1 :           # 기존 값이 0 또는 1 인 경우 -> 합
        ans += tmp
    else:
        if tmp > 1:         # 추가 값이 0 또는 1이 아닌 경우 -> 곱
            ans *= tmp 
        else:               # 추가 값이 0 또는 1인 경우 -> 합
            ans += tmp  
        
print(ans)

# 답안 예시
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])
for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
        
print(result)



# 이코테. 볼링공 고르기
# 볼링공의 개수 n, 공의 최대 무게 m이 공백으로 구분되어 각각 자연수 형태로 주어짐
# (1 <= n <= 1000, 1 <= m <= 10)
# 볼링공의 무게 k가 공백으로 구분돼 자연수 형태로 주어짐 (1 <= k <= m)

# 문제 : 볼링공 무게가 다른 것을 고르는 경우의 수를 찾되, 같은 무게이더라도 다른 볼링공으로 간주한다.
# 출력 값 : 볼링공을 고르는 경우의 수
# 아이디어 : 값

import sys
import time
from itertools import combinations

n, m = map(int, input().split())
weight = list(map(int, sys.stdin.readline().split()))

# 단순 구현 (for문 2번 돌리기)
start = time.time()

res = 0 
for i in range(n):
    for j in range(i+1, n):
        if weight[i] != weight[j]:
            res += 1
               
print(res)

end = time.time()
print(f"{end - start : .10f} sec")

# 조합 사용
cmb = list(combinations(weight, 2))
weight = set(weight)
print(len(cmb)-(n-len(weight)))


# 답안 예시
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1
    
result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i]               # 무게가 i인 볼링공의 개수 제외 (= A가 선택할 수 있는 개수 제외)
    result += array[i] * n      # B가 선택하는 경우의 수와 곱하기
    
print(result)



# 이코테. 무지의 먹방 라이브
# 답안 예시
from operator import itemgetter

def solution(food_times, k):
    # if sum(food_times) < k:
    #     return -1
    
    foods = []
    n = len(food_times)
    
    for i in range(n):
        foods.append((food_times[i], i+1))       # 음식을 먹는 시간과 음식 번호를 순서대로 기입한다.
        
    foods.sort()                                 # 음식을 먹는 시간에 따라 값 정렬
    
    pretime = 0                                 # 이전 소요 시간
    for i, food in enumerate(foods):
        diff = food[0] - pretime                # 해당 번호의 음식을 먹기 위해 필요한 시간 (높이)
        
        if diff != 0:                           # 이전 음식을 먹고 현재 음식을 먹기 위해 소요시간이 필요한 경우
            spend = diff * n                    # 소요 시간 = 음식을 먹기 위해 필요한 시간 (높이) * 음식의 개수 (n)
            
            if spend <= k:                      # 소요시간이 남은시간 보다 작은 경우
                k -= spend
                pretime = food[0]
                
            else:
                # 남은 음식들을 원래 순서대로 정렬 (itemgetter를 사용해서 원래 인덱스를 바탕으로 정렬)
                sublist = sorted(foods[i:], key = foods[i:][1])
                k %= n
                
                return sublist[k][1]
                
                
        n -= 1                                  # 음식의 개수 하나씩 제거
    
    return -1 

food_times = [3, 1 ,2]
k = 5
print(solution(food_times, k))

