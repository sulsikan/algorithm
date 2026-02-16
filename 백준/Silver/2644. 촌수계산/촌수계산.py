import sys
input = sys.stdin.readline

def dfs(a, b, cnt):
    global min_cnt
    visited.append(a)
    for person in graph[a]:
        if person == b:
            min_cnt = min(min_cnt, cnt+1)
            return
        if person not in visited:
            dfs(person, b, cnt+1)

# 사람 수
n = int(input())
# 촌수 계산할 두 사람의 번호
target_a, target_b = map(int, input().split())
# 부모자식 관계인 사람
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = []
min_cnt = 1e9
cnt = 0

dfs(target_a, target_b, 0)
if min_cnt != 1e9:
    print(int(min_cnt))
else:
    print(-1)