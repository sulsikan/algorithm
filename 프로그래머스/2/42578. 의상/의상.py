
def solution(clothes):
    dict = {}
    # 종류별 세기
    for item, kind in clothes:
        dict[kind] = dict.get(kind, 0) + 1
    
    # 경우의 수 계산 (안입음, 1번 입음, 2번 입음, ... => n+1)
    answer = 1
    for cnt in dict.values():
        answer *= (cnt + 1)
    
    return answer-1