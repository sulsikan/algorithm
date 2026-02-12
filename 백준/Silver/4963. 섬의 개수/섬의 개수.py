import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]


def dfs(y, x):
    visited[y][x] = True
    for id in range(8):
        nx = x + dx[id]
        ny = y + dy[id]
        if 0 <= nx < w and 0 <= ny < h:
            if not visited[ny][nx] and sealand[ny][nx] == 1:
                dfs(ny, nx)


w, h = map(int, input().split())
while w != 0 and h != 0:
    cnt = 0
    sealand = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    for j in range(h):
        for i in range(w):
            if visited[j][i] == False and sealand[j][i] == 1:
                dfs(j, i)
                cnt += 1
    print(cnt)
    # 너비 높이 업데이트
    w, h = map(int, input().split())