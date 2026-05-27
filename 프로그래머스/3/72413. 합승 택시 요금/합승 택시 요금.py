# point : 시작지점 -> 거점 -> 목적지가 최단거리가 되는 "거점" 찾기
# 다익스트라
import heapq

def solution(n, s, a, b, fares):
    INF = 1e9
    
    graph = [[] for _ in range(n+1)]
    
    for v, u, c in fares:
        graph[v].append((u, c))
        graph[u].append((v, c))
        
    def dijkstra(start):
        queue = [(0, start)]
        distance = [INF] * (n+1)
        distance[start] = 0
        
        while queue:
            cur_cost, cur_node = heapq.heappop(queue)
            
            for nxt_node, cost in graph[cur_node]:
                nxt_cost = cur_cost + cost
                if nxt_cost < distance[nxt_node]:
                    distance[nxt_node] = nxt_cost
                    heapq.heappush(queue, (nxt_cost, nxt_node))
                    
        return distance
    
    distance_list = [0] + [dijkstra(i) for i in range(1, n+1)]
    
    answer = INF
    for i in range(1, n+1):
        answer = min(answer, distance_list[s][i] + distance_list[i][a] + distance_list[i][b])
    
    return answer