from collections import deque
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
max_weight = 0   #다리 중 최대 중량 저장

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    max_weight = max(max_weight, c)

start, end = map(int, input().split())

# “limit 이상의 다리만 사용할 때 이동 가능한가?” 판단 함수
def bfs(limit):
    visited = [False] * (n+1)
    queue = deque([start])
    visited[start] = True

    while queue:
        now = queue.popleft()
        if now == end:
            return True

        for next_node, weight in graph[now]:
            if not visited[next_node] and weight >= limit:
                visited[next_node] = True
                queue.append(next_node)

    return False

left, right = 1, max_weight
answer = 0

while left <= right:
    mid = (left + right) // 2

    if bfs(mid):  # 가능하면
        answer = mid
        left = mid + 1
    else:          # 불가능하면
        right = mid - 1

print(answer)