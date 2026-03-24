import heapq
import sys
input = sys.stdin.readline

def dijkstra(s):
    dist = [1e9] * (N+1)
    dist[s] = 0
    queue = []
    heapq.heappush(queue, (0, s))

    while queue:
        d, v = heapq.heappop(queue)
        for nd, nv in graph[v]:
            if d + nd < dist[nv]:
                dist[nv] = d + nd
                heapq.heappush(queue, (dist[nv], nv))

    return dist

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, time = map(int, input().split())
    graph[start].append((time, end))

result = [0]*(N+1)
for i in range(1, N+1):
    dist = dijkstra(i)
    if i == X:
        for j in range(1,N+1):
            result[j] += dist[j]
        continue
    result[i] += dist[X]

print(max(result))