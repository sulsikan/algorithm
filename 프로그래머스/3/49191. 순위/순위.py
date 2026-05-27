def solution(n, results):
    answer = 0
    winner = [[] for _ in range(n+1)]
    loser = [[] for _ in range(n+1)]
    
    # 그래프 구성
    for w, l in results:
        winner[w].append(l)
        loser[l].append(w)
        
    def dfs(graph, start, visited):
        count = 0
        
        for nxt in graph[start]:
            if visited[nxt] == False:
                visited[nxt] = True
                count += 1
                count += dfs(graph, nxt, visited)
                
        return count
    
    for player in range(1, n+1):
        visited = [False] * (n + 1)
        win_cnt = dfs(winner, player, visited)
        
        visited = [False] * (n + 1)
        lose_cnt = dfs(loser, player, visited)
        
        if win_cnt + lose_cnt == n-1:
            answer += 1
        
    return answer