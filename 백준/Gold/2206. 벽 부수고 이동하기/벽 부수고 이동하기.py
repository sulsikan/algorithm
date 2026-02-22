import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
nm_map = [list(map(int, input().strip())) for _ in range(N)]

# 벽을 부순 상태로 방문 했는지
visited = [[[False]*2 for _ in range(M)] for _ in range(N)]
dist = [[[0]*2 for _ in range(M)] for _ in range(N)]

queue = deque()
queue.append((0,0,0))
visited[0][0][0] = True
dist[0][0][0] = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

while queue:
    y, x, b = queue.popleft()

    if y == N-1 and x == M-1:
        print(dist[y][x][b])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if not visited[ny][nx][b] and nm_map[ny][nx] == 0:
                queue.append((ny, nx, b))
                visited[ny][nx][b] = True
                dist[ny][nx][b] = dist[y][x][b] + 1
            if nm_map[ny][nx] == 1 and b == 0 and not visited[ny][nx][1]:
                visited[ny][nx][1] = True
                dist[ny][nx][1] = dist[y][x][b] + 1
                queue.append((ny, nx, 1))

else:
    print(-1)
