import heapq
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

dx = [-1, 0, 1, 0]  #세로
dy = [0, 1, 0, -1]  #가로
dist = [[1e9]*M for _ in range(N)]
dist[0][0] = 0
queue = []
heapq.heappush(queue, (0, 0, 0))

while queue:
    breaking, y, x = heapq.heappop(queue)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if maze[ny][nx] == 0:
                if dist[ny][nx] > breaking:
                    dist[ny][nx] = breaking
                    heapq.heappush(queue, (breaking, ny, nx))
            else:
                if dist[ny][nx] > breaking + 1:
                    dist[ny][nx] = breaking + 1
                    heapq.heappush(queue, (dist[ny][nx], ny, nx))

print(dist[N-1][M-1])