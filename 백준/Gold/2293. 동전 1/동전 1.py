import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin_arr = [int(input()) for _ in range(n)]

dp = [0] * (k+1)
dp[0] = 1

for coin in coin_arr:
    for i in range(coin, k+1):
        dp[i] += dp[i-coin]

print(dp[k])