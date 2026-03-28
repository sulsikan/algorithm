import sys
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

dp[0][0] = graph[0][0]

for i in range(1, n):
    dp[0][i] = dp[0][i-1] + graph[0][i]
    dp[i][0] = dp[i-1][0] + graph[i][0]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + graph[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = dp[x2-1][y2-1]
    both = 0
    if 1 < x1:
        result -= dp[x1-2][y2-1]
        both += 1
    if 1 < y1:
        result -= dp[x2-1][y1-2]
        both += 1
    if both == 2:
        result += dp[x1-2][y1-2]
    print(result)