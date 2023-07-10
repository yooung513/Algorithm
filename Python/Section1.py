# Section 1.코드 구현 능력 기르기

# K번째 약수
# 나의 풀이
# : 약수를 전체 다 구한 후 정렬 한 다음 k번째 수를 구함
n, k = map(int, input().split())

div = []
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        if n // i == i:
            div.append(i)
        else:
            div.append(i)
            div.append(n // i)

div.sort()
if len(div) >= k:
    print(div[k - 1])
else:
    print(-1)

# 강의
# : 약수를 구하는 과정에서 k번째가 된 경우 바로 출력
#   for-else 구문을 이용해 for문으로 카운팅하지 못하는 경우 빠져나갈 수 있도록 했다.
n, k = map(int, input().split())
cnt = 0
for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1

    if cnt == k:
        print(i)
        break
else:
    print(-1)



# K번째 수
# 나의 풀이 (강의와 유사)
# : 리스트를 덮어써도 될 수 있는 것을 인지하고 있자.
#   또한, print 표현식도 인지하고 있자.
t = int(input())
for _ in range(t):
    n, s, e, k = map(int, input().split())
    num = list(map(int, input().split()))

    new = num[s - 1 : e]
    new.sort()
    print(new[k - 1])
    print("%d" % (new[k - 1]))



# K번째 큰 수
# 나의 풀이 = 강의
# : 처음에 i, j, k를 변수로 사용해 k값이 변하는 문제가 있었다.
#   변수 설정할 때 주의할 것
n, k = map(int, input().split())
card = list(map(int, input().split()))
res = set()

for x in range(n):
    for y in range(x + 1, n):
        for z in range(y + 1, n):
            res.add(card[x] + card[y] + card[z])

res = list(res)
res.sort(reverse=True)

print(res[k - 1])



# 대표값
# 나의 풀이 (강의와 유사)
n = int(input())
sco = list(map(int, input().split()))

avg = round(sum(sco)/n)

mabs = abs(avg - sco[0])
midx = 0
for idx, val in enumerate(sco):
    if abs(avg-val) <= mabs:
        if sco[midx] < val:
            mabs = abs(avg-val)
            midx = idx

print(avg, midx+1)

# round 함수는 round_half_even 방식이므로 정확하게 반을 나타내면 짝수로 표기한다.
# 예) a = round(4.500)
#   > a = 4
#    b = round(66.5)
#   > b = 67
# 따라서, 첫째 자리에서 정확하게 반올림 하기 위해서는 정수형 변환을 사용한다.
# 예) c = 66.5
#    c = c + 0.5    -> 반올림 값 
#    c = int(c)     -> 소수점을 없애는 작업

# 기존 풀이
n = int(input())
score = list(map(int, input().split()))

avr = int((sum(score)/n)+0.5)
chk = []
for i in range(avr):
  for idx, val in enumerate(score):
    if avr+i == val:
      chk.append((val, idx+1))
    if avr-i == val:
      chk.append((val, idx+1))
  
  if len(chk) > 0:
    break

chk.sort(key = lambda x : (-x[0], x[1]))
print(avr, chk[0][1])



# 정다면체
# 나의 풀이 (강의와 같음)
n, m = map(int, input().split())
chk = [0] * (n+m+1)
for i in range(1, n+1):
    for j in range(1, m+1):
        chk[i+j] += 1

mcnt = max(chk)
for idx, val in enumerate(chk):
    if val == mcnt:
        print(idx, end=" ")



# 자릿수의 합
# 나의 풀이 -> 강제 변환 사용
n = int(input())
num = list(map(int, input().split()))

res = []
for i, x in enumerate(num):
    tmp = list(str(x))
    snum = 0
    for t in  tmp:
        snum += int(t)
    res.append((snum, i))

res.sort(key= lambda x: (-x[0], x[1]))
print(num[res[0][1]])

# 나의 풀이 -> 함수 사용
def digit_sum(x):
    res = 0
    while x > 0:
        res += x%10
        x = x//10
    return res

n = int(input())
num = list(map(int, input().split()))

mx = 0
ans = 0
for x in num:
    tot = digit_sum(x)
    if tot > mx:
        mx = tot
        ans = x

print(x)



# 소수 (에라토스테네스 체)
# 나의 풀이
# 강의 풀이는 변수를 지정해서 카운트
n = int(input())
chk = [1] * (n+1)

for i in range(2, n+1):
    if chk[i] == 1:
        for j in range(i*2, n+1, i):
            chk[j] = 0

print(sum(chk[2:]))



# 뒤집은 소수
# 나의 풀이 
def reverse(x):
    res = 0
    while x > 0:
        res *= 10
        res += x % 10 
        x = x // 10
    return res

def isPrime(x):
    chk = [0] * (x+1)
    for i in range(2, x+1):
        if chk[i] == 0:
            for j in range(i*2, x+1, i):
                chk[j] = 1

    if chk[x] == 0:
        return True
    else: 
        return False

n = int(input())
num = list(map(int, input().split()))

for n in num:
    x = reverse(n)
    
    if isPrime(x) == True:
        print(x, end=" ")



# 주사위 게임
# 나의 풀이
n = int(input())

res = 0 
for _ in range(n):
    a, b, c = map(int, input().split())
    
    if a == b and b == c:
        tmp = 10000 + a*1000
    elif a != b and b != c and c != a:
        tmp = max(a, b, c) * 100
    else : 
        if b == c:
            tmp = 1000 + b*100
        else:
            tmp = 1000 + a*100

    res = max(res, tmp)

print(res) 



# 점수계산
# 나의 풀이
n = int(input())
sco = list(map(int, input().split()))

res = 0
plus = 0
for s in sco:
    if s == 0:
        plus = 0
    else: 
        plus += s

    res += plus

print(res)
