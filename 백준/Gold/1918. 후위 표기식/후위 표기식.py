# 1918 후위 표기식
import sys
input = sys.stdin.readline

infix_notation = input().strip()
operator = {'+':1, '-':1, '*':2, '/':2}

stack = []
out = []

for ch in infix_notation:
    if ch.isalnum():
        out.append(ch)
    elif ch == '(':
        stack.append(ch)
    elif ch == ')':
        while stack and stack[-1] != '(':
            out.append(stack.pop())
        stack.pop()
    else:
        while stack and stack[-1] != '(' and operator[stack[-1]] >= operator[ch]:
            out.append(stack.pop())
        stack.append(ch)

while stack:
    out.append(stack.pop())

print(''.join(out))
