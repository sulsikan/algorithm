import sys
from itertools import combinations

input = sys.stdin.readline
N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
candidates = [(r, c) for r in range(1, N-1) for c in range(1, N-1)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(li):
    global answer
    visited = []
    total = 0
    for r, c in li:
        visited.append((r, c))
        total += field[r][c]
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if (nr, nc) not in visited:
                visited.append((nr, nc))
                total += field[nr][nc]
            else:
                return
    answer = min(answer, total)


answer = int(1e9)
for li in combinations(candidates, 3):
    check(li)

print(answer)