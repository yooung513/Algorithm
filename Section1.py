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
#대표값
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
