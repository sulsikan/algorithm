import sys
input = sys.stdin.readline

d, n, m = map(int, input().split())
rocks = [int(input()) for _ in range(n)] + [d]
rocks.sort()

left, right, answer = 0, d, 0

while left <= right:
    mid = (left + right) // 2
    prev, cnt = 0, 0            # 현재위치, 바위를 제거한 개수
    for rock in rocks:
        if rock - prev < mid:
            cnt += 1
        else:
            prev = rock

    if cnt <= m:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1


print(answer)
