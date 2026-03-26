# case1 = 1 → v1 → v2 → N
# case2 = 1 → v2 → v1 → N

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n, e = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int,input().split())


def dijkstra(start):
    dist = [INF] * (n+1)
    dist[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        d, node = heapq.heappop(queue)

        if dist[node] < d:
            continue

        for c, b in graph[node]:
            if dist[b] > c + d:
                dist[b] = c+d
                heapq.heappush(queue, (dist[b], b))
    return dist

dist_1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

case1 = dist_1[v1] + dist_v1[v2] + dist_v2[n]
case2 = dist_1[v2] + dist_v2[v1] + dist_v1[n]
answer = min(case1, case2)

if answer >= INF:
    print(-1)
else:
    print(answer)