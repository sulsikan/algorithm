import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
result = []
stack = []
    
for j in range(n):
    for i in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            stack.append((i, j))
            cnt = 1

            while stack:
                x, y = stack.pop()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        stack.append((nx, ny))
                        cnt += 1

            result.append(cnt)

print(len(result))
for i in sorted(result):
    print(i)