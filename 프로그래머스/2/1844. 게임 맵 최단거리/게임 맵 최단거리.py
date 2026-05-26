# 최단 경로를 구하는 전형적인 문제로, DFS보다 BFS가 적합
from collections import deque
    
def solution(maps):
    INF = 1e9
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    m = len(maps)
    n = len(maps[0])
    
    queue = deque([(0, 0)])
    dist = [[INF] * n for _ in range(m)]
    dist[0][0] = 1
    
    while queue:
        y, x = queue.popleft()
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            next_dist = dist[y][x] + 1
            if 0 <= nx < n and 0 <= ny < m:
                if maps[ny][nx] == 1 and next_dist < dist[ny][nx]:
                    queue.append((ny, nx))
                    dist[ny][nx] = next_dist
                    
    if dist[m-1][n-1] < INF:
        return dist[m-1][n-1]
    else:
        return -1