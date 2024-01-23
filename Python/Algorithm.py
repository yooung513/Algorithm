## 정렬

# 1. 선택 정렬
# 2. 삽입 정렬
# 3. 퀵 정렬

# 4. 계수 정렬
# 모든 원소의 값이 0보다 크거나 같다고 가정

arr = [7, 8, 2, 4, 1, 3, 6, 1, 9, 5]
cnt = [0] * (max(arr)+1)        # 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)

for i in range(len(arr)):
    cnt[arr[i]] += 1            # 각 데이터에 해당하는 인덱스 값 증가
    
for i in range(len(cnt)):
    for j in range(cnt[i]):
        print(i, end = ' ')