import sys
input = sys.stdin.readline
board = [[0] * 100 for _ in range(100)]
n = int(input())
for _ in range(n):
    w, h = map(int, input().split())
    h_in = 0
    while h_in < 10:
        for i in range(10):
            board[w+i][h+h_in] = 1
        h_in += 1

sum_blk = 0
for i in range(100):
    sum_blk += sum(board[i])

print(sum_blk)