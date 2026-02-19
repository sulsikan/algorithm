from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
# visited = [[0] * m for _ in range(n)]
boxes = [list(map(int, input().split())) for _ in range(n)]

day = 0
queue = deque()
tmp_queue = deque()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for j in range(n):
    for i in range(m):
        if boxes[j][i] == 1:
            queue.append((j, i))

while queue:
    y, x = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and boxes[ny][nx] == 0:
            boxes[ny][nx] = 1
            tmp_queue.append((ny, nx))

    if not queue and tmp_queue:
        day += 1
        queue += tmp_queue
        tmp_queue = deque()

# 토마토가 모두 다 익지 못했다면
for row in boxes:
    if 0 in row:
        print(-1)
        sys.exit(0)

print(day)