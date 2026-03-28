import sys
input = sys.stdin.readline

n = int(input())
dp = [False] * (n+1)


if n == 1:
    print("SK")
    exit()
elif n == 2:
    print("CY")
    exit()

dp[1] = True
dp[2] = False
dp[3] = True

for i in range(4, n+1):
    # 1개 또는 3개 빼서 상대를 지는 상태로 만들 수 있으면 이김
    if not dp[i-1] or not dp[i-3]:
        dp[i] = True

print("SK" if dp[n] else "CY")