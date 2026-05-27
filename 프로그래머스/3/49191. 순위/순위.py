# bfs
from collections import deque
def solution(n, results):
    answer = 0
    winner_graph = [[] for _ in range(n+1)]
    loser_graph = [[] for _ in range(n+1)]
    
    for w, l in results:
        winner_graph[w].append(l)
        loser_graph[l].append(w)
        
    def bfs(graph, start):
        visited = [False] * (n+1)
        queue = deque([start])
        count = 0
        
        visited[start] = True
    
        while queue:
            player = queue.popleft()

            for nxt in graph[player]:
                if not visited[nxt]:
                    visited[nxt] = True
                    queue.append(nxt)
                    count += 1
        return count
    
    for p in range(1, n+1):
        win_count = bfs(winner_graph, p)
        
        lose_count = bfs(loser_graph, p)
        
        if win_count + lose_count == n-1:
            answer += 1
    
    return answer