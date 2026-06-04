def solution(dirs):
    visited = set()
    x, y = 0, 0
    
    move = {
        "U" : (0, 1),
        "D" : (0, -1),
        "L" : (-1, 0),
        "R" : (1, 0)
    }
    
    for d in dirs:
        dx, dy = move[d]
        nx, ny = x + dx, y + dy
        
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue

        visited.add((x, y, nx, ny))
        visited.add((nx, ny, x, y))
        
        x, y = nx, ny
    
    return len(visited) // 2
        