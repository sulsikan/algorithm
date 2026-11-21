import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rs = []
chk = [False] * (N + 1)

def bt(num):
    if num == M:
        print(' '.join(map(str, rs)))
        return 
    else:
        for i in range(1, N + 1):
            if not chk[i]:
                chk[i] = True
                rs.append(i)
                bt(num+1)
                chk[i] = False
                rs.pop()
bt(0)