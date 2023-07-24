# 이분탐색 (결정 알고리즘) 및 그리디 알고리즘

# 이분검색
# 나의 풀이 -> 답만 추출할 수 있도록 함 (이분검색은 아님)
n, m = map(int, input().split())
a = list(map(int, input().split()))

res = 1
for x in a:
    if x < m :
        res += 1

print(res)

# 이분검색이란? 
# 검색할 자료를 반씩 나누어 나머지 반만 검새하는 방식을 반복하여 자료를 찾는 검색 방법
# 이분검색 : O(log n)
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

lt = 0
rt = n-1        #인덱스 값이므로

while lt <= rt:
    mid = (lt+rt) // 2 
    if a[mid] == m:
        print(mid+1)
        break
    else:
        if a[mid] > m:
            rt = mid - 1
        else:
            lt = mid + 1