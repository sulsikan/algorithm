import sys
input = sys.stdin.readline

S = list(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"
result = []

for ch in alphabet:
    for idx in range(len(S)):
        if ch in S:
            if ch == S[idx]:
                result.append(idx)
                break
        else:
            result.append(-1)
            break
for i in result:
    print(i, end=' ')