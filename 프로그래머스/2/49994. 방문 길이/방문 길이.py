def solution(dirs):
    visited = set()
    x, y = 0, 0
    answer = 0
    
    move = {
        "U" : (0, 1),
        "D" : (0, -1),
        "R" : (1, 0),
        "L" : (-1, 0)
    }
    
    for d in dirs:
        nxt_x = x + move[d][0]
        nxt_y = y + move[d][1]
        
        if -5 <= nxt_x <= 5 and -5 <= nxt_y <= 5:
            if (x, y, nxt_x, nxt_y) not in visited:
                visited.add((x, y, nxt_x, nxt_y))
                visited.add((nxt_x, nxt_y, x, y))
                answer += 1
            
            x, y = nxt_x, nxt_y
            
    return answer
        
        