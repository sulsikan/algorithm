# S를 기준으로 최단 경로
# 미지의 수 K를 기준으로 최단경로
# 다익스트라
import heapq

def solution(n, s, a, b, fares):
    INF = 1e9
    
    graph = [[] for _ in range(n+1)]
    for u, v, c in fares:
        graph[u].append((v, c))
        graph[v].append((u, c))
        
    def dijkstra(start):
        hq = [(0, start)]
        distance = [INF] * (n+1)
        distance[start] = 0

        while hq:
            cur_cost, cur_node = heapq.heappop(hq)

            for nxt_node, cost in graph[cur_node]:
                nxt_cost = cost + cur_cost
                if distance[nxt_node] > nxt_cost:
                    distance[nxt_node] = nxt_cost
                    heapq.heappush(hq, (nxt_cost, nxt_node))
                    
        return distance
    
    
    dist_list = [[] for _  in range(n+1)]
    
    for node in range(1, n+1):
        dist_list[node] = dijkstra(node)
        
    answer = dist_list[s][a] + dist_list[s][b]
    
    for k in range(1, n+1):
        if k == s:
            continue
        
        new_cost = dist_list[s][k] + dist_list[k][a] + dist_list[k][b]
        if new_cost < answer:
            answer = new_cost
    
    return answer