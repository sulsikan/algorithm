n = int(input())

time = [0] * (n+1)
profit = [0] * (n+1)

for i in range(1, n+1):
    t, p = map(int,input().split())
    time[i] = t
    profit[i] = p

dp = [0] * (n+2)

for i in range(n, 0, -1):
    if i + time[i] <= n+1:
        dp[i] = max(
            dp[i+1],                # 상담 안함
            profit[i] + dp[i+time[i]]  # 상담 함
        )
    else:
        dp[i] = dp[i+1]

print(dp[1])