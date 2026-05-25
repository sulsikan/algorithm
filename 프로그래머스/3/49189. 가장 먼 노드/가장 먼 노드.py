from collections import deque

def solution(n, edge):
    answer = 0
    
    # create a graph
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    # initialize data structure
    dist = [-1] * (n+1)
    dist[1] = 0
    queue = deque([1])
    
    # play bfs
    while queue:
        now = queue.popleft()
        
        for nxt in graph[now]:
            if dist[nxt] == -1:
                dist[nxt] = dist[now] + 1
                queue.append(nxt)
                
    for d in dist:
        if d == max(dist):
            answer += 1
    
    return answer