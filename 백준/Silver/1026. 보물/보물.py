import sys
input = sys.stdin.readline

N = int(input())
A_arr = list(map(int, input().split()))
B_arr = list(map(int, input().split()))

sorted_a = sorted(A_arr, reverse=True)
sorted_b = sorted(B_arr)

S = 0
for i in range(N):
    S += sorted_a[i] * sorted_b[i]

print(S)