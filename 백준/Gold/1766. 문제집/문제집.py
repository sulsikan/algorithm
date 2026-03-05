import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

# 입력: 선후관계
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

# 우선순위 큐 (최소 힙)
hq = []

# 진입차수가 0인 문제들을 힙에 넣기
for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(hq, i)

# hq = [3, 4, 5]
result = []
while hq:
    cur = heapq.heappop(hq)
    result.append(cur)
    for nxt in graph[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(hq, nxt)

print(*result)