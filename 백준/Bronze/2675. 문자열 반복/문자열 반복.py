import sys
input = sys.stdin.readline

n = int(input())
P = []
for _ in range(n):
    R, S = input().split()
    R = int(R)
    result_str = []
    for s in S:
        result_str.append(s*R)
    P.append(''.join(result_str))

for p in P:
    print(p)