import sys
input = sys.stdin.readline

n = int(input())
res = 0


for _ in range(n):
    word = list(input().strip())
    saved = []
    chk = 0
    if len(word) == 1:
        res += 1
        continue

    for w in range(len(word)):
        if word[w] not in saved:
            saved.append(word[w])
        else:
            if word[w] != word[w-1]:
                chk = 1
                
            
    if chk == 0 :
        res += 1
print(res)