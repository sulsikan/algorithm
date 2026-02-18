from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
birds = [deque(list(map(str, input().split()))) for _ in range(n)]
sentence = deque(list(map(str, input().split())))

while sentence:
    comp = sentence.popleft()

    for i in range(n):
        if birds[i] and comp == birds[i][0]:
            birds[i].popleft()
            break
    else:
        print("Impossible")
        sys.exit(0)

for i in range(n):
    if birds[i]:
        print("Impossible")
        sys.exit(0)

print("Possible")