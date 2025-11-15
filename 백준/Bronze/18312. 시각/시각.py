import sys
input = sys.stdin.readline
N, K = input().split()

count = 0
for h in range(int(N)+1):
    for m in range(60):
        for s in range(60):
            time_str = f'{h:02}{m:02}{s:02}'
            if K in time_str:
                count += 1
print(count)