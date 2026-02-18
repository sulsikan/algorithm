from collections import deque
import sys
input = sys.stdin.readline

n, w, l = map(int, input().split())
trucks = deque(list(map(int, input().split())))

bridge = deque()
time = 0
arrival = []

while len(arrival) < n:
    if bridge:
        if bridge[0] == 0:
            bridge.popleft()
        if len(bridge) >= w:
            arrival.append(bridge.popleft())
        if trucks and len(bridge) <= w and sum(bridge)+trucks[0] <= l:
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)
    else:
        if trucks:
            bridge.append(trucks.popleft())

    time += 1

print(time)