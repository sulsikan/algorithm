n = int(input())
meeting_schedule = [list(map(int, input().split())) for _ in range(n)]
meeting_schedule.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0
for start, end in meeting_schedule:
    if start >= end_time:
        count += 1
        end_time = end

print(count)