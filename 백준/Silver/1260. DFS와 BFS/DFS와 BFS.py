import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

# dfs
visited_dfs = [False] * (N+1)
dfs_order = []

def dfs(x):
    visited_dfs[x] = True
    dfs_order.append(x)
    for nx in graph[x]:
        if not visited_dfs[nx]:
            dfs(nx)
dfs(V)

# bfs
visited_bfs = [False] * (N+1)
bfs_order = []
queue = deque([V])
visited_bfs[V] = True

while queue:
    x = queue.popleft()
    bfs_order.append(x)
    for nx in graph[x]:
        if not visited_bfs[nx]:
            visited_bfs[nx] = True
            queue.append(nx)

print(*dfs_order)
print(*bfs_order)
