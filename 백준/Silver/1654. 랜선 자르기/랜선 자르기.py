import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lanlines = [int(input()) for _ in range(k)]

start = 1
end = sum(lanlines) // n
answer = 0

while start <= end:
    mid = (start+end) // 2
    lan_calc = 0

    for lan in lanlines:
        lan_calc += lan // mid

    if lan_calc >= n:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)