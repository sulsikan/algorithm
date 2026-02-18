from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque(range(1, n+1))
game_class = 0

while len(queue) > 1:
    game_class += 1
    t = ((game_class**3)-1) % len(queue)
    for _ in range(t):
        queue.append(queue.popleft())
    queue.popleft()

print(queue[0])