import sys
input = sys.stdin.readline

N = int(input())
map = [list(map(int, input().strip())) for _ in  range(N)]
#chk = [[False] * N for _ in range(N)]
each = 0

def dfs(y, x):
    # 종료 조건
    if y < 0 or x < 0 or y >= N or x >= N or map[y][x]!=1: return
    global each
    each += 1
    # 동서남북 탐색
    map[y][x] = 0
    dfs(y+1, x)
    dfs(y - 1, x)
    dfs(y, x+1)
    dfs(y, x-1)

# 탐색 시작
ans = []
for j in range(N):
    for i in range(N):
        if map[j][i] == 1:
            each = 0
            dfs(j, i)
            ans.append(each)
ans.sort()
print(len(ans))
for i in ans:
    print(i)