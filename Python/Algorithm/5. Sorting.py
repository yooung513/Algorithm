# 정렬

# 이코테. 위에서 아래로
import sys

n = int(input())
arr = list(int(sys.stdin.readline()) for _ in range(n))

arr.sort(reverse=True)

print(*arr)


# 답안 예시 
n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))
    
arr = sorted(arr, reverse=True)

for i in arr:
    print(i, end= ' ')
    
    
    
# 이코테. 성적이 낮은 순서로 학생 출력하기
n = int(input())
arr = []
for _ in range(n):
    name, score = input().split()
    arr.append((int(score), name))
    
arr = sorted(arr)
for tmp in arr:
    print(tmp[1], end=' ')
    

# 답안 예시
n = int(input())
arr = []
for _ in range(n):
    input_data = input().split()
    arr.append(input_data[0], int(input_data[1]))

arr = sorted(arr, key=lambda student: student[1])
# arr = sorted(arr, key=lambda x: x[1])

for student in arr:
    print(student[0], end=' ')
    
    
    
# 이코테. 두 배열의 원소 교체
n, k = map(int, input().split())
aList = list(map(int, input().split()))
bList = list(map(int, input().split()))

aList = sorted(aList)                   # 오름차순
bList = sorted(bList, reverse=True)     # 내림차순

for i in range(k):
    if aList[i] < bList[i]:
        aList[i], bList[i] = bList[i], aList[i]
        
    else:
        break
    
print(sum(aList))



