import sys
input = sys.stdin.readline
a, b = map(int, input().split())

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

for i in range(gcd(a, b)):
    print(1, end='')