import sys
input = sys.stdin.readline

n = int(input())
group_words = [list(input().strip()) for _ in range(n)]
prev_words = [[] for _ in range(n)]
count = 0
for i in range(n):
    for idx, c in enumerate(group_words[i]):
        if c in prev_words[i] and idx >= 1 and c != group_words[i][idx-1]:

            count += 1
            break
        else:
            prev_words[i].append(c)
print(n-count)