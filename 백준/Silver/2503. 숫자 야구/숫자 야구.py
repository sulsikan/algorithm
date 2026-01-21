import sys
input = sys.stdin.readline

n = int(input())
answer = []

for num in range(123, 999):
    num = str(num)
    if '0' in num:
        continue
    if num[0] in num[1:] or num[1] in num[2:]:
        continue
    answer.append(num)

for _ in range(n):
    num, s, b = map(int, input().split())

    nums = list(str(num))
    tmp = []

    for chk in answer:
        cnt_s, cnt_b = 0, 0
        for i in range(3):
            if nums[i] == chk[i]:
                cnt_s += 1
            elif nums[i] != chk[i] and nums[i] in chk:
                cnt_b += 1

        if cnt_s == s and cnt_b == b:
            tmp.append(chk)
    answer = tmp

print(len(answer))