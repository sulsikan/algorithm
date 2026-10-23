from collections import deque

def solution(land):
    
    n = len(land)      # 세로
    m = len(land[0])   # 가로
    
    visited = [[False] * m for _ in range(n)]
    column_oil = [0] * m
    
    dx = [-1, 1, 0, 0]
    dy = [0 ,0, -1, 1]
    
    for r in range(n):
        for c in range(m):
            # 아직 방문하지 않은 석유
            if land[r][c] == 1 and not visited[r][c]:
                # 1. BFS 시작
                queue = deque([(r, c)])
                visited[r][c] = True
                
                size = 0
                columns = set()

                # 2. 석유 덩어리 크기 계산
                while queue:
                    x, y = queue.popleft()
                    
                    # 3. 석유가 걸친 열을 set에 저장
                    size += 1
                    columns.add(y)
                    
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        
                        if 0 <= nx < n and 0 <= ny < m:
                            if land[nx][ny] == 1 and not visited[nx][ny]:
                                queue.append((nx, ny))
                                visited[nx][ny] = True
                                
                # 4. 각 열의 column_oil에 덩어리 크기 추가 
                for col in columns:
                    column_oil[col] += size
                       
        
    return max(column_oil)