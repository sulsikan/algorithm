'''
공항으로 가는 배열
1. icn이 있는 배열을 찾는다
2. 목적지를 answer에 추가한다
3. 목적지의 마지막 값이 있는 배열을 찾는다
4. 반복한다.
'''
from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)

    # 1) 그래프 구성
    for a, b in tickets:
        graph[a].append(b)

    # 2) 사전순 경로를 위해: pop()으로 가장 작은 목적지가 나오게
    #    목적지를 내림차순 정렬해두면 pop()은 가장 작은 것부터 꺼냄
    for a in graph:
        graph[a].sort(reverse=True)

    route = []
    stack = ["ICN"]

    # 3) Hierholzer 방식 DFS
    while stack:
        cur = stack[-1]
        if graph[cur]:              # 갈 곳이 남아 있으면
            stack.append(graph[cur].pop())
        else:                       # 더 이상 갈 곳이 없으면 경로 확정
            route.append(stack.pop())

    # 4) 역순으로 쌓였으니 뒤집기
    return route[::-1]
