from collections import deque

def solution(maps):
    answer = 0
    
    m = len(maps)
    n = len(maps[0])
    
    INF = 1e9
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    queue = deque([(0, 0)])
    distance = [[INF] * n for _ in range(m)]
    distance[0][0] = 1
    
    while queue:
        y, x = queue.popleft()
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < n and 0 <= ny < m:
                if maps[ny][nx] == 1 and distance[y][x] + 1 < distance[ny][nx]:
                    queue.append((ny, nx))
                    distance[ny][nx] = distance[y][x] + 1
                    
    if distance[m-1][n-1] < INF:
        return distance[m-1][n-1] 
    else:
        return -1