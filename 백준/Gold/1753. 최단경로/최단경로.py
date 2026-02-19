
import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
k = int(input())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = 10**18
dist = [INF] * (V+1)
dist[k] = 0

pq = [(0, k)]  # (거리, 정점)

while pq:
    d, x = heapq.heappop(pq)
    if d != dist[x]:  # 0 == 0
        continue
    for nx, w in graph[x]:
        nd = d + w
        if nd < dist[nx]:
            dist[nx] = nd
            heapq.heappush(pq, (nd, nx))

out = []
for i in range(1, V+1):
    out.append("INF" if dist[i] == INF else str(dist[i]))
print("\n".join(out))
