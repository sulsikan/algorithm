n, m = map(int,input().split())
immigration_time = [int(input()) for _ in range(n)]

start, end = 0, min(immigration_time)*m
while start <= end:
    mid = (start+end) // 2
    sum = 0
    for immi_time in immigration_time:
        sum += mid // immi_time

    if sum >= m:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1

print(answer)