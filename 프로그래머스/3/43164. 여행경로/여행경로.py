from collections import defaultdict

def solution(tickets):
    # 출발지 : 목적지로 나누어진 딕셔너리 형태로 tickets를 재선언
    graph = defaultdict(list)
    for fr, to in tickets:
        graph[fr].append(to)
    
    # pop으로 answer에 추가할 것이기 때문에 목적지 알파벳 역순으로 정렬.
    for a in graph:
        graph[a].sort(reverse=True)
        
    # pop으로 answer에 경로 추가
    stack = ["ICN"]
    route = []
    
    while stack:
        top = stack[-1]
        if graph[top]:
            stack.append(graph[top].pop())  # 가장 사전순 작은 목적지로 이동
        else:
            route.append(stack.pop())       # 더 갈 곳 없으면 경로 확정
            
    return route[::-1]