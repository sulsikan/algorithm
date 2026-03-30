import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
coins.reverse()
count = 0

for each_coin in coins:
    count += k // each_coin
    k = k % each_coin

print(count)