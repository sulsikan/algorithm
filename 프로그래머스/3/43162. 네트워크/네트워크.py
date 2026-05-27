def solution(n, computers):

    graph = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i].append(j)
                
    def dfs(graph, node, visited):
        for nxt in graph[node]:
            if visited[nxt] == False:
                visited[nxt] = True
                dfs(graph, nxt, visited)
                
        return visited
    
    answer = 0
    visited = [False] * n
    
    for node_num in range(n):
        if not visited[node_num]:
            visited = dfs(graph, node_num, visited)
            answer += 1
        
    return answer
        