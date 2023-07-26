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