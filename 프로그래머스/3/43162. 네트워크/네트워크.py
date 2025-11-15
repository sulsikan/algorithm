# 노드간선그래프-> dfs/bfs -> 다른 하나라도 이어져있으면 T 아니면 F
def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if visited[i] == False:
            DFS(n, computers, i, visited)
            answer += 1
    return answer

def DFS(n, computers, i, visited):
    visited[i] = True
    for connect in range(n):
        if computers[i][connect] == 1 and visited[connect] == False:
            DFS(n, computers, connect, visited)