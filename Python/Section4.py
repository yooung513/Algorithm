# Section 4. 자료구조 활용

# 가장 큰 수 (Stack)
num, m = map(str, input().split())
num = list(num)
m = int(m)
stk = list(num[0])

for i in range(1, len(num)):
    while len(stk) > 0 and num[i] > stk[-1] and m != 0:
        m -= 1
        stk.pop()
    stk.append(num[i])

if m != 0:
    stk = stk[:-m]
print(''.join(stk))



# 쇠막대기
# ** 강의



# 후위 표기식 만들기
# 1차 풀이 -> *나 /의 경우 앞수와 계산되는 것이므로 후위 표기식 작성 시 문제 발생
a = list(input())
sign = []
res = []

for x in a:
    if x.isdecimal():
        res.append(x)
        if sign:
            if sign[-1] == "*" or sign[-1] == "/":
                res.append(sign.pop())
    else:
        if x == '(':
            sign.append(x)
        elif x == ')':
            while 1:
                tmp = sign.pop()
                if tmp == '(':
                    break
                else:
                    res.append(tmp)
        else:
            sign.append(x)

while sign:
    tmp = sign.pop()
    res.append(tmp)

print(''.join(res))
# 강의



# 후위식 연산
pos = list(input())
num = []

for x in pos:
    if x.isdecimal():
        num.append(x)
    else:
        n1 = int(num.pop())
        n2 = int(num.pop())
        if x == '+':
            num.append(n2+n1)
        elif x == '-':
            num.append(n2-n1)
        elif x == '*':
            num.append(n2*n1)
        else:
            num.append(n2/n1)

print(num[0])



# 공주구하기
from collections import deque

n, k = map(int, input().split())
prince = [i for i in range(1, n+1)]
prince = deque(prince)

cnt = 0
while len(prince) > 1:
    now = prince.popleft()
    cnt += 1

    if cnt == k:
        cnt = 0
    else:
        prince.append(now)

print(prince[0])



# 응급실
from collections import deque

n, m = map(int, input().split())
dan = list(map(int, input().split()))

stay = []
for idx, val in enumerate(dan):
    stay.append((idx, val))

dan.sort()
stay = deque(stay)
cnt = 0 
while stay and dan:
    tmp = stay.popleft()
    i = tmp[0]
    d = tmp[1]

    if d == dan[-1]:
        dan.pop()
        cnt += 1
        if i == m:
            print(cnt)
            break
    else:
        stay.append(tmp)

# 리스트 컴프리헨션
dan = [(idx, val) for idx, val in enumerate (list(map(int, input().split())))]

# 강의
# ***any 구문을 사용해서 더 큰 값이 있는지 확인함 (for문 병합)
from collections import deque

n, m = map(int, input().split())
dq = [(idx, val) for idx, val in enumerate (list(map(int, input().split())))]

dq = deque(dq)
cnt = 0

while True:
    now = dq.popleft()
    if any(now[1] < x[1] for x in dq):
        dq.append(now)
    else:
        cnt += 1
        if now[0] == m:
            print(cnt)
            break



# 교육과정설계
org = list(input())
n = int(input())
for i in range(n):
    std = list.copy(org)
    chk = list(input())
    for x in chk:
        if x == std[0]:
            std.pop(0)

        if len(std) == 0:
            print('#%d YES' %(i+1))
            break
    else:
        print('#%d NO' %(i+1))



# 단어찾기
n = int(input())
dic = dict()
for _ in range(n):
    word = input()
    dic[word] = 0

for _ in range(n-1):
    word = input()
    dic[word] += 1

for k, w in dic.items():
    if w == 0:
        print(k)
        break



# 애너그램
# 카운터 함수 사용
from collections import Counter

x = input()
a = Counter(x)
y = input()
b = Counter(y)

if a == b:
    print("Yes")
else:
    print("No")

# 딕셔너리 사용
# 해당 딕셔너리 문제는 -1, 1의 경우 sum 값이 0으로  수렴돼서 오류가 남
word1 = input()
word2 = input()
dic = dict()

for x in word1:
    if x in dic.keys():
        dic[x] += 1
    else:
        dic[x] = 1

for y in word2:
    if y in dic.keys():
        dic[y] -= 1
    else:
        print("NO")
        break

if sum(dic.values()) == 0:
    print("YES")
else:
    print("NO")

# 딕셔너리 초기값 설정 표현 및 논리 오류 수정
word1 = input()
word2 = input()
dic = dict()

for x in word1:
    dic[x] = dic.get(x, 0)+1

for y in word2:
    dic[y] = dic.get(y, 0)-1

for val in dic.values():
    if val != 0:
        print("NO")
        break
else:
    print("YES")

# 리스트 해쉬 방법
# 아스키 코드
# 대문자 A = 65, Z = 90 / 소문자 a = 97, z = 122
a = input()
b = input()
str1 = [0]*52
str2 = [0]*52

for x in a:
    if x.isupper():
        str1[ord(x)-65] += 1
    else:
        str1[ord(x)-71] += 1

for x in b:
    if x.isupper():
        str2[ord(x)-65] += 1
    else:
        str2[ord(x)-71] += 1

for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")

# 파이썬은 리스트 비교가 가능
if str1 == str2:
    print("YES")
else:
    print("NO")



# 최소 힙
num = []
chk = -1
res = []

while 1:
    n = int(input())
    if n == -1:
        break
    else:
        if n == 0:
            if len(num) == 0:
                res.append(-1)
            else:
                res.append(num[0])
                chk = 0
                num = []
        else:
            if chk == -1:
                num.append(n)
                chk = n
            else:
                if n < chk:
                    num[0] = n
                    num.append(chk)
                else:
                    num.append(n)

for x in res:
    print(x)

# 힙 사용
import heapq as hq

a = []

while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)



# 최대 힙