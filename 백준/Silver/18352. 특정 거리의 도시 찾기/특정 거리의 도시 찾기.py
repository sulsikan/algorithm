import heapq
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

queue = []
INF = int(1e9)
dist = [INF] * (N+1)
heapq.heappush(queue, (0, X))
dist[X] = 0

answer = []
while queue:
    d, c = heapq.heappop(queue)
    if dist[c] == K:
        answer.append(c)
    elif d < K:
        for nc in graph[c]:
            if dist[nc] > d+1:
                dist[nc] = d+1
                heapq.heappush(queue, (dist[nc], nc))

if answer:
    for a in answer:
        print(a)
else:
    print(-1)


