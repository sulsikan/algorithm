from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
card_queue = deque([i for i in range(1, n+1)])

while len(card_queue) > 1:
    card_queue.popleft()
    card_queue.append(card_queue.popleft())

print(card_queue[0])