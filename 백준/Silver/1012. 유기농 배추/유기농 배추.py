import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1,0,-1,0]
ans =[]

def dfs(x, y):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nx < M and 0 <= ny < N and board[nx][ny] == True:
            board[nx][ny] = False
            dfs(nx, ny)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[False] * N for _ in range(M)]
    # 지도 만들기
    for _ in range(K):
        i, j = map(int, input().split())
        board[i][j] = True
    # 실행
    cnt = 0

    for i in range(M):
        for j in range(N):
            if board[i][j] == True:
                dfs(i, j)
                cnt += 1
    ans.append(cnt)

for i in ans:
    print(i)