import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
normal_image = [list(input().strip()) for _ in range(N)]
queue = deque()


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(image):
    result = []
    visited = [[False] * N for _ in range(N)]
    for j in range(N):
        for i in range(N):
            if not visited[j][i]:
                queue.append((j, i))
                visited[j][i] = True
                while queue:
                    y, x = queue.popleft()
                    for dr in range(4):
                        nx = x + dx[dr]
                        ny = y + dy[dr]
                        if 0 <= nx < N and 0 <= ny < N and image[ny][nx] == image[y][x] and not visited[ny][nx]:
                            queue.append((ny, nx))
                            visited[ny][nx] = True

                result.append(image[j][i])

    return len(result)


normal_cnt = bfs(normal_image)

redgreen_image = [row[:] for row in normal_image]
for i in range(N):
    for j in range(N):
        if normal_image[i][j] == 'G':
            redgreen_image[i][j] = 'R'

rg_cnt = bfs(redgreen_image)

print(normal_cnt, rg_cnt)