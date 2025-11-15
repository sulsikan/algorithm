from collections import deque
# 노드간선그래프-> dfs/bfs -> 다른 하나라도 이어져있으면 T 아니면 F
def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if visited[i] == False:
            BFS(n, computers, i, visited)
            answer += 1
    return answer

def BFS(n, computers, i, visited):
    queue = deque()
    queue.append(i)
    while queue:
        com = queue.popleft()
        visited[com] = True
        for connect in range(n):
            if visited[connect]==False and computers[com][connect] == 1:
                queue.append(connect)
                
        
            