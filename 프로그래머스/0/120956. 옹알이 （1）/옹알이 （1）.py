'''
1. 아이디어
- 가능발음과 입력을 비교 > 입력에서 가능발음 공백으로 대체(소거하면 안됨) > 입력이 비어지게되면 answer+=1
'''

def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    cnt = 0
    
    for i in babbling:
        for j in words:
            i=i.replace(j, " ")
        if not i.strip():
            cnt += 1
    
    return cnt