
import sys
input = sys.stdin.readline

n = int(input())
cups = [0, 1, 2, 3]
for _ in range(n):
    cup_num1, cup_num2 = map(int, input().split())
    cup_idx1 = cups.index(cup_num1)
    cup_idx2 = cups.index(cup_num2)
    tmp_cup = cups[cup_idx1]
    cups[cup_idx1] = cups[cup_idx2]
    cups[cup_idx2] = tmp_cup

print(cups[1])