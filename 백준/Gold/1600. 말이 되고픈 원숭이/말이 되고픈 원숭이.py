import sys
from collections import deque
input = sys.stdin.readline

K = int(input())
W, H = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(H)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

horse_moves = [
    (-2, -1), (-2, 1), (2, -1), (2, 1),
    (-1, -2), (-1, 2), (1, -2), (1, 2)
]
# visited[x][y][k] = 방문 여부. 같은 위치라도 k 다르면 다른 상태
visited = [[[False] * (K + 1) for _ in range(W)] for _ in range(H)]

def bfs():
    queue = deque()
    queue.append((0, 0, K, 0))  # x, y, 남은 말 이동, 거리
    visited[0][0][K] = True

    while queue:
        x, y, k, cnt = queue.popleft()

        if x == H - 1 and y == W - 1:
            return cnt

        # 일반 이동
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < H and 0 <= ny < W:
                if grid[nx][ny] == 0 and not visited[nx][ny][k]:
                    visited[nx][ny][k] = True
                    queue.append((nx, ny, k, cnt + 1))

        # 말 이동
        if k > 0:
            for dxh, dyh in horse_moves:
                nx = x + dxh
                ny = y + dyh

                if 0 <= nx < H and 0 <= ny < W:
                    if grid[nx][ny] == 0 and not visited[nx][ny][k - 1]:
                        visited[nx][ny][k - 1] = True
                        queue.append((nx, ny, k - 1, cnt + 1))

    return -1

print(bfs())