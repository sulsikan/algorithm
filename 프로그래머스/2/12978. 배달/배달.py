import heapq

def solution(N, road, K):
    answer = 0
    INF = int(1e9)
    
    # create a graph
    graph = [[] for _ in range(N+1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
        
    # initialize data structure
    distance = [INF] * (N+1)
    distance[1] = 0
    pq = []
    heapq.heappush(pq, (0, 1))
    
    # shortest distance calculation
    while pq:
        cost, node = heapq.heappop(pq)
        
        if distance[node] < cost:
            continue
            
        for next_node, next_cost in graph[node]:
            next_cost += cost
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heapq.heappush(pq, (next_cost, next_node))
            
    for d in distance:
        if d <= K:
            answer += 1
    
    return answer