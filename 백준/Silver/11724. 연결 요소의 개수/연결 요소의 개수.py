import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
visited = [False] * (N+1)

def dfs(x, graph, visited):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i, graph, visited)

for i in range(1, N+1):
    if not visited[i]:
        dfs(i, graph, visited)
        count += 1

print(count)