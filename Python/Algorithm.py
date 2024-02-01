## 정렬
# 1. 선택 정렬
# 2. 삽입 정렬
# 3. 퀵 정렬

# 4. 계수 정렬
#    계수정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용이 가능하며, 
#    일반적으로, 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때 효과적이다.
#    O(N+K)의 시간 복잡도와 공간 복잡도를 가진다.

# 모든 원소의 값이 0보다 크거나 같다고 가정
arr = [7, 8, 2, 4, 1, 3, 6, 1, 9, 5]
cnt = [0] * (max(arr)+1)        # 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)

for i in range(len(arr)):
    cnt[arr[i]] += 1            # 각 데이터에 해당하는 인덱스 값 증가
    
for i in range(len(cnt)):
    for j in range(cnt[i]):
        print(i, end = ' ')
        
        
        
## 탐색
# 1. 순차 탐색
#    리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법

def Sequential_Search(n, target, array):
    for i in range(n):              # 각 원소를 하나씩 확인
        if array[i] == target:      # 현재의 원소가 찾고자 하는 원소와 동일한 경우
            return i + 1            # 현재의 위치 반환 (i는 인덱스)
        
input_data = input().split()        # 리스트 형식으로 input
n = int(input_data[0])
target = input_data[1]

array = input().split()
print(Sequential_Search(n, target, array))


# 2. 이진 탐색
#    반으로 쪼개면서 탐색하기
#    내부의 데이터가 정렬되어있어야만 사용할 수 있는 알고리즘

# 재귀함수 활용
def Binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2 
    
    if array[mid] == target:        # 찾은 경우 중간점 인덱스 반환
        return mid
    
    elif array[mid] > target:       # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        return Binary_search(array, target, start, mid-1)
    
    else:                           # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        return Binary_search(array, target, mid + 1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = Binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

# 반복문 활용
def Binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2 
        
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = Binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
    
    
    
# 다이나믹 프로그래밍

# 피보나치 함수를 재귀함수로 구현
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(5))


# 피보나치 함수 - 동적 계획법
# 메모이제이션하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수 - 탑다운 / q
def fibo(x):
    if x == 1 or x == 2:                    # 종료 조건
        return 1
    
    if d[x] != 0:                           # 이미 계산한 적 있는 문제의 경우
        return d[x]
    
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))


# 피보나치 함수 - 반복문 (바텀업 / 상향식)
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
    
print(d[n])