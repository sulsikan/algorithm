import sys
input = sys.stdin.readline

n, m = map(int, input().split())

result = []

def recur(start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    for i in range(start, n+1):
        if i not in result:
            result.append(i)
            recur(i+1)
            result.pop()
            
recur(1)