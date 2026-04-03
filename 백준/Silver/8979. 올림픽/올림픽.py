import sys
input = sys.stdin.readline

N, K = map(int, input().split())
medal_state = [list(map(int, input().split())) for _ in range(N)]

medal_state.sort(key=lambda x : (x[1], x[2], x[3]), reverse=True)

rank, tmp = 1, 0
for i in range(1, N + 1):
    if medal_state[i-1][0] == K:
        print(rank)
        break
    if medal_state[i-1][1:] != medal_state[i][1:]:
        rank += (1 + tmp)
        tmp = 0
    else:
        tmp += 1