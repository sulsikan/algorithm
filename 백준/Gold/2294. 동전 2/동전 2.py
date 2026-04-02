import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin_arr = [int(input()) for _ in range(n)]

dp = [100000 for _ in range(k+1)]
dp[0] = 0

for coin in coin_arr:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[k] == 100000:
    print(-1)
else:
    print(dp[k])