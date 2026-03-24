import heapq
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, time = map(int, input().split())
    graph[start].append((time, end))

INF = int(1e9)
go = [INF] * (N+1)
come = [INF] * (N+1)
queue = []
go[X], come[X] = 0, 0

# go
for i in range(1, N+1):
    if i == X:
        continue
    heapq.heappush(queue, (0, i))
    vtox = [INF] * (N+1)
    vtox[i] = 0
    while queue:
        dist, village = heapq.heappop(queue)
        if village == X and dist < go[i]:
            go[i] = dist
            continue
        for nt, nv in graph[village]:
            if nt + dist < vtox[nv]:
                vtox[nv] = nt + dist
                heapq.heappush(queue, (vtox[nv], nv))

# come
heapq.heappush(queue, (0, X))

while queue:
    dist, village = heapq.heappop(queue)
    for nt, nv in graph[village]:
        if nv == X:
            continue
        if come[nv] > nt+dist:
            come[nv] = nt+dist
            heapq.heappush(queue, (come[nv], nv))

answer = []
for i in range(1, N+1):
    answer.append(go[i]+come[i])

print(max(answer))