# 1012 유기농 배추
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y, visited):
    visited[x][y] = 1
    if 0 <= x < M and 0 <= y < N:
        # 상
        if 1 <= y < N:
            if land[x][y-1] == 1 and visited[x][y-1] == 0:
                dfs(x, y - 1, visited)
        # 하
        if 0 <= y < N-1:
            if land[x][y+1] == 1 and visited[x][y+1] == 0:
                dfs(x, y + 1, visited)
        # 좌
        if 1 <= x < M:
            if land[x-1][y] == 1 and visited[x-1][y] == 0:
                dfs(x - 1, y, visited)
        # 우
        if 0 <= x < M-1:
            if land[x+1][y] == 1 and visited[x+1][y] == 0:
                dfs(x + 1, y, visited)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    land = [[0] * N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        land[x][y] = 1

    visited = [[0] * N for _ in range(M)]
    cnt = 0

    for i in range(M):
        for j in range(N):
            if land[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j, visited)
                cnt += 1
    print(cnt)
