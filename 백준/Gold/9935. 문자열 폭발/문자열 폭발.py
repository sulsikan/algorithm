# 9935 문자열 폭발
import sys
input = sys.stdin.readline

normal = list(input().strip())
explosion = input().strip()
answer = ''
stack = []

for ch in normal:
    stack.append(ch)
    if stack[-1] == explosion[-1]:
        if stack[-len(explosion):] == list(explosion):
            for _ in range(len(explosion)):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
