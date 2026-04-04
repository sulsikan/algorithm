def solution(targets):
    answer = 0
    targets = sorted(targets, key=lambda x : (x[1], x[0]))
    
    s, e = 0, 0
    for nx, ny in targets:
        if nx >= e:
            e = ny
            answer += 1
            
    return answer