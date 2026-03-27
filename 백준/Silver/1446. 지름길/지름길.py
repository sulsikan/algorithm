import sys, heapq
input = sys.stdin.readline

n, d = map(int, input().split())
inf = float("inf")

graph = [[] for _ in range(d+1)]
distance = [inf]*(d+1)

for i in range(d):
    graph[i].append((1, i+1))
    # 왜 초기화?

for _ in range(n):
    start, dest, dist = map(int, input().split())
    if dest > d:
        continue
    graph[start].append((dist, dest))

queue = []
heapq.heappush(queue, (0, 0))
distance[0] = 0

while queue:
    now_dist, now_location= heapq.heappop(queue)

    for next_dist, next_dest in graph[now_location]:
        cost = distance[now_location] + next_dist
        if distance[next_dest] > cost:
            distance[next_dest] = cost
            heapq.heappush(queue, (cost, next_dest))

print(distance[d])