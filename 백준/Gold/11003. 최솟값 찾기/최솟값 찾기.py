import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
arr = list(map(int, input().split()))

queue = deque()

for idx in range(N):
    while queue and queue[-1][1] > arr[idx]:
        queue.pop()

    queue.append((idx, arr[idx]))

    if queue[0][0] <= idx - L:
        queue.popleft()

    print(queue[0][1], end=" ")