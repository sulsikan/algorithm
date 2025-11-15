import sys
input = sys.stdin.readline
a, b = map(int, input().split())

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

def lcm(x, y):
    return x * y // gcd(x, y)

print(gcd(a, b))
print(lcm(a, b))