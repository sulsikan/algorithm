k, n = map(int,input().split())
lan_lines = [int(input()) for _ in range(k)]

start, end, answer = 1, max(lan_lines), 0
while start <= end:
    mid = (start+end) // 2
    lan_cnt = 0
    for lan in lan_lines:
        lan_cnt += lan // mid

    if lan_cnt >= n:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)