
d, n, m = map(int, input().split())
rocks = [int(input()) for _ in range(n)] +[d]
rocks.sort()

left, right, answer = 0, d, 0
while left <= right:
    mid = (left+right) // 2
    prev, remove_cnt = 0, 0
    for rock in rocks:
        if rock - prev < mid:
            remove_cnt += 1
        else:
            prev = rock

    if remove_cnt <= m:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1


print(answer)