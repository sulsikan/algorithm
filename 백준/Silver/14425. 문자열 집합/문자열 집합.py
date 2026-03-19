n, m = map(int, input().split())

words = {}
for _ in range(n):
    words[input()] = True

chk_cnt = 0
for _ in range(m):
    chk_word = input()
    if chk_word in words:
        chk_cnt += 1

print(chk_cnt)
