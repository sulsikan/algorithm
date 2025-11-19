import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    test_result = input()
    score = 0
    sum_score = 0
    for tr in test_result:
        if tr == 'O':
            score += 1
        else:
            score = 0
        sum_score += score
    print(sum_score)