import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input())
# 1
num_list = list(permutations(range(1,10), 3))

for _ in range(N):
    # 2
    chk, s, b = map(int, input().split())
    chk = list(map(int, str(chk)))
    tmp = []
    for num in num_list:
        cnt_s, cnt_b = 0, 0
        for i in range(3):
            if num[i] == chk[i]:
                cnt_s += 1
                continue
            if num[i] != chk[i] and chk[i] in num:
                cnt_b += 1
        if cnt_s == s and cnt_b == b:
            tmp.append(num)
    num_list = tmp

print(len(num_list))