
import sys
input = sys.stdin.readline

s = list(input().strip())
stack = []
answer = 0
mult = 1
prev = ''

for ch in s:
    if ch == '(':
        stack.append('(')
        mult *= 2
        prev = '('

    elif ch == '[':
        stack.append('[')
        mult *= 3
        prev = '['

    elif ch == ')':
        if not stack or stack[-1] !='(':
            print(0)
            sys.exit(0)
        if prev == '(':
            answer += mult
        mult //= 2
        stack.pop()
        prev = ')'

    elif ch == ']':
        if not stack or stack[-1] !='[':
            print(0)
            sys.exit(0)
        if prev == '[':
            answer += mult
        mult //= 3
        stack.pop()
        prev = ']'

print(answer if not stack else 0)