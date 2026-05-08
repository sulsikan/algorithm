from collections import deque

def solution(n, edge):
    answer = 0
    
    # create a graph
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    # initialize data structure
    queue = deque([1])
    dist = [-1] * (n+1)
    dist[1] = 0
    
    # play
    while queue:
        now = queue.popleft()
        
        for next in graph[now]:
            if dist[next] == -1:
                dist[next] = dist[now] + 1
                queue.append(next)
            
    for d in dist:
        if d == max(dist):
            answer += 1
    
    return answer