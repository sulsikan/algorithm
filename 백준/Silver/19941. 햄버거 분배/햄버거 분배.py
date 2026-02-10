import sys

input = sys.stdin.readline

n, k = map(int, input().split())
table = list(input().strip())

person = {}
prev = []
p_cnt = 0
for i in range(n):
    if table[i] == 'P':
        p_cnt += 1
        person[i] = []

        for j in range(k, 0, -1):
            if len(prev) >= j and 'H' == prev[-j]:
                person[i].append(i - j)

        for j in range(1, k + 1):
             if i+j < n and 'H' == table[i+j]:
                person[i].append(i + j)
    prev.append(table[i])

eaten = set()
cnt = 0
if not person:
    print(0)
    sys.exit(0)

for key in person:
    if person[key]:
        for hamburger in person[key]:
            if hamburger not in eaten:
                eaten.add(hamburger)
                cnt += 1
                break
print(cnt)