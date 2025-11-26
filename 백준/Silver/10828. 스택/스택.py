import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    cmd = input().strip()
    if cmd == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif cmd == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:    # push
        cmd, num = cmd.split()
        stack.append(num)