import sys, math
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort() #음수 방지

# 1. 차이 구하기
diff = []
for i in range(1, N):
    diff.append(arr[i]-arr[i-1])

# 2. 차이들의 gcd 구하기
g = diff[0]
for d in diff[1:]:
    g = math.gcd(g, d)

# 3. gcd 약수 모두 출력
result = []
for i in range(2, int(g**0.5) +1):
    if g % i == 0:
        result.append(i)
        if i != g//i:
            result.append(g//i)
            
result.append(g)
result.sort()
print(*result)