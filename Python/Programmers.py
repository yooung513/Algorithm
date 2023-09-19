# 프로그래머스

# 체육복
# Lv1. 그리디
def solution(n, lost, reserve):
    # 정렬
    lost.sort()
    reserve.sort()
    
    # 제한사항 3, 4번
    for res in reserve[:]:
        if res in lost:
            reserve.remove(res)
            lost.remove(res)
            
    # 앞/뒤 번호 
    for r in reserve:
        for x in (r-1, r+1):
            if x in lost:
                lost.remove(x)
                break
            
    return n-len(lost)