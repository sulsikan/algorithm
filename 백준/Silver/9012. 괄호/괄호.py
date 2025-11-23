import sys
input = sys.stdin.readline

n = int(input())
answer = []
for seq in range(n):
    vps = list(input().strip())
    if vps.count('(') == vps.count(')'):
        answer.append('YES')
        while vps:
            vps.pop()
            if vps.count('(') < vps.count(')'):
                answer[seq] = 'NO'
                break
    else:
        answer.append('NO')

for i in range(n):
    print(answer[i])