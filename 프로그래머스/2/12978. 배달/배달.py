import heapq

def solution(N, road, K):

    INF = int(1e9)

    graph = [[] for _ in range(N+1)]

    for a, b, c in road:

        graph[a].append((b, c))
        graph[b].append((a, c))

    distance = [INF] * (N+1)

    distance[1] = 0

    pq = []

    heapq.heappush(pq, (0, 1))

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for next_node, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(
                    pq,
                    (new_cost, next_node)
                )

    answer = 0

    for d in distance:
        if d <= K:
            answer += 1

    return answer