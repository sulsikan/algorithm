import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
lab_map = [list(map(int, input().split())) for _ in range(N)]

zero_positions = []
virus_positions = []
for i in range(N):
    for j in range(M):
        if lab_map[i][j]==0:
            zero_positions.append((i,j))
        if lab_map[i][j]==2:
            virus_positions.append((i,j))

selected_wall_position = list(combinations(zero_positions, 3))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
cnt_zero = 0

for walls in selected_wall_position:
    tmp_map = [row[:] for row in lab_map]

    for y, x in walls:
        tmp_map[y][x] = 1

    q = deque(virus_positions)  # 원본은 유지

    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and tmp_map[ny][nx] == 0:
                tmp_map[ny][nx] = 2
                q.append((ny,nx))

    cnt_zero = max(cnt_zero, sum(row.count(0) for row in tmp_map))

print(cnt_zero)
