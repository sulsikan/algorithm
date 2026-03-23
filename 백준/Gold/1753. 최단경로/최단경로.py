import heapq
import sys
input = sys.stdin.readline

V, E = map(int,input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = int(1e9)
costs = [INF] * (V+1)
queue = []

heapq.heappush(queue, (0, K))
costs[K] = 0

while queue:
    w, v = heapq.heappop(queue)
    if costs[v] < w:
        continue
    for node, cost in graph[v]:
        if costs[node] > w + cost :
            costs[node] = w + cost
            heapq.heappush(queue, (costs[node], node))

for i in range(1, V+1):
    if costs[i] != INF:
        print(costs[i])
    else:
        print('INF')