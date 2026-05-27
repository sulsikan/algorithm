def solution(n, computers):
    graph = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
                
    stack = [0]
    visited = [False] * n 
    answer = 0
    
    for node in range(n):
        if visited[node] == False:
            stack.append(node)
        else:
            continue
            
        while stack:
            now = stack.pop()
            for nxt in graph[now]:
                if visited[nxt] == False:
                    visited[nxt] = True
                    stack.append(nxt)

        answer += 1
    
    
    return answer