import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
answer = 0

while start <= end:
    mid = (end + start) // 2
    sum_length = 0

    for tree in trees:
        if tree > mid:
            sum_length += (tree - mid)

    if sum_length >= m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)