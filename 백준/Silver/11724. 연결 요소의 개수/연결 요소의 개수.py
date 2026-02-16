
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(x):
    visited[x] = True
    for node in graph[x]:
        if not visited[node]:
            dfs(node)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
stack = []
visited = [False] * (n+1)
cnt = 0

for idx in range(1, n+1):
    if not visited[idx]:
        dfs(idx)
        cnt += 1

print(cnt)