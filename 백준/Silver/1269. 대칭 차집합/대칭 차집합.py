import sys
input = sys.stdin.readline

a,b = map(int,input().split())
a_arr = set(map(int, input().split()))
b_arr = set(map(int, input().split()))

diff_set = []
for a_element in a_arr:
    if a_element not in b_arr:
        diff_set.append(a_element)

for b_element in b_arr:
    if b_element not in a_arr:
        diff_set.append(b_element)

print(len(diff_set))