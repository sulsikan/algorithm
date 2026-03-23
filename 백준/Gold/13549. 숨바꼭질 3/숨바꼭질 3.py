# 5 -> 4 -> 8 -> 16-> 17 총 2초
# 5-> 10->  9->  18-> 17

import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 100000
INF = int(1e18)
dist = [INF] * (MAX + 1)

def dijkstra(start):
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        time, x = heapq.heappop(pq)
        if dist[x] < time:
            continue
        if x == K:
            return time

        nx = x * 2
        if 0 <= nx <= MAX and dist[nx] > time:
            dist[nx] = time
            heapq.heappush(pq, (time, nx))

        nx = x - 1
        if 0 <= nx <= MAX and dist[nx] > time + 1:
            dist[nx] = time + 1
            heapq.heappush(pq, (time + 1, nx))

        nx = x + 1
        if 0 <= nx <= MAX and dist[nx] > time + 1:
            dist[nx] = time + 1
            heapq.heappush(pq, (time + 1, nx))

    return dist[K]

print(dijkstra(N))