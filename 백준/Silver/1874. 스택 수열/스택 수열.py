import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

nums.reverse()
stack = []
answer = []
push_num = 1
# stack에 값 push하기
for i in range(1, n+1):
    stack.append(i)
    answer.append('+')
    while True:
        # nums[-1] 랑 stack[-1]이 같으면 stack pop
        if stack:
            if stack[-1] == nums[-1]:
                stack.pop()
                nums.pop()
                answer.append('-')
            else: break
        else: break

if stack:
    print('NO')
else:
    for i in range(len(answer)):
        print(answer[i])