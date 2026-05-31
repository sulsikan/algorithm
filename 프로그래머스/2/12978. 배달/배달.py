# 다익스트라 최단경로 모든 마을 구하기
# 조건 확인해서 answer 카운트

import heapq

def solution(N, road, K):
    INF = 1e9
    
    graph = [[] for _ in range(N+1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
        
    queue = [(0, 1)]
    distance = [INF] * (N+1)
    distance[1] = 0
    
    while queue:
        cur_cost, cur_node = heapq.heappop(queue)
        
        for nxt_node, cost in graph[cur_node]:
            nxt_cost = cost + cur_cost
            if distance[nxt_node] > nxt_cost:
                distance[nxt_node] = nxt_cost
                heapq.heappush(queue, (nxt_cost, nxt_node))
    
    answer = 0
    for d in distance:
        if d <= K:
            answer += 1
            
    return answer