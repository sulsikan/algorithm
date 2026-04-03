import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

stack = []
result = [-1] * N
for i in range(N):
    while stack:
        if arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            result[idx] = arr[i]
        else:
            break

    stack.append(i)

print(*result)
