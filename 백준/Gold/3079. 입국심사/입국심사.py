import sys
input = sys.stdin.readline

n, m = map(int,input().split())
immigration_time = [int(input()) for _ in range(n)]

start, end = 0, min(immigration_time) * m
while start <= end:
    mid = (start+end) // 2
    sum_people_count = 0
    for immi_time in immigration_time:
        sum_people_count += mid // immi_time  # 처리 가능한 인원 수

    if sum_people_count >= m:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)