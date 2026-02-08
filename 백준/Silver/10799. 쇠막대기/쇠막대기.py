
import sys
input = sys.stdin.readline

lasers = input().strip()

stack = []
prev = ''
answer = 0
for ls in lasers:
    # (
    if ls == '(':
        stack.append(0)
        prev = '('
    else:
        stack.pop()
        if prev == '(':
            answer += len(stack)
        else:
            answer += 1
        prev = ')'

print(answer)
