import sys

input = sys.stdin.readline

N = int(input())
K = int(input())
infection = [0] * N
tree = []
for _ in range(K):
    tree.append(list(map(int, input().split())))

def dfs(com):
    infection[com-1] = 1
    for a, b in tree:
        if a == com and infection[b-1] == 0:
            dfs(b)
        elif b == com and infection[a-1] == 0:
            dfs(a)

dfs(1)
print(sum(infection) - 1)