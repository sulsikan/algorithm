import sys
input = sys.stdin.readline

answer = []

while True:
    sentence = input().rstrip('\n')
    if sentence == '.':
        break

    stack = []

    for char in sentence:
        if char == '(' or char == '[':
            stack.append(char)

        elif char == ')':
            if not stack or stack[-1] != '(':
                answer.append('no')
                break
            stack.pop()

        elif char == ']':
            if not stack or stack[-1] != '[':
                answer.append('no')
                break
            stack.pop()
    else:
        if not stack:
            answer.append('yes')
        else:
            answer.append('no')

for a in answer:
    print(a)