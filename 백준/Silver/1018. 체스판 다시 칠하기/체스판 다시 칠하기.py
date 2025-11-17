import sys
input = sys.stdin.readline

n,m = map(int, input().split())
board = [input().strip() for _ in range(n)]

pattern1 = ["WBWBWBWB", "BWBWBWBW"] * 4
pattern2 = ["BWBWBWBW", "WBWBWBWB"] * 4

min_count = float('inf')

for i in range(n-7):
    for j in range(m-7):
        count1= 0
        count2 =0
        for di in range(8):
            for dj in range(8):
                if board[i+di][j+dj] != pattern1[di][dj]:
                    count1 += 1
                if board[i+di][j+dj] != pattern2[di][dj]:
                    count2 += 1
        min_count = min(min_count, count1, count2)

print(min_count)