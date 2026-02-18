from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque(range(1, n+1))
result = []
while queue:
    result.append((queue.popleft()))
    if queue:
        queue.append(queue.popleft())

print(' '.join(map(str, result)))