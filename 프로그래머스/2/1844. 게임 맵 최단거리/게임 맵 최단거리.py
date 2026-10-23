from collections import deque

def solution(maps):
    
    m = len(maps)
    n = len(maps[0])
    
    INF = 1e9
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    dist = [[INF] * n for _ in range(m)]
    dist[0][0] = 1
    queue = deque([(0, 0)])
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            nxt_x = x + dx[i]
            nxt_y = y + dy[i]
            
            nxt_dist = dist[y][x] + 1
            
            if 0 <= nxt_x < n and 0 <= nxt_y < m:
                if maps[nxt_y][nxt_x] == 1 and nxt_dist < dist[nxt_y][nxt_x]:
                    dist[nxt_y][nxt_x] = nxt_dist
                    queue.append((nxt_y, nxt_x))
    
    if dist[m-1][n-1] < INF:
        return dist[m-1][n-1]
    else:
        return -1