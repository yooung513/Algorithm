# Section 2. 탐색 & 시뮬레이션

# 회문 문자열 검사



































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