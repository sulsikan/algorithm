import sys
input = sys.stdin.readline

n = int(input())
channal = [input().strip() for _ in  range(n)]

idx1, idx2 = channal.index('KBS1'), channal.index('KBS2')

if idx1 > idx2:
    idx2 += 1

print('1'*idx1 + '4'*idx1 + '1'*idx2 + '4'*(idx2-1))