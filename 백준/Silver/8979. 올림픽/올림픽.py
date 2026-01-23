import sys
input = sys.stdin.readline

# input
n, k = map(int, input().split())
medals = [list(map(int, input().split())) for _ in range(n)]

# 정렬
medals.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

# k 점수 찾기
for nation, g, s, b in medals:
    if nation == k:
        k_score = (g, s, b)
        break

# k_score가 처음 나오는 위치가 순위
for i, (nation, g, s, b) in enumerate(medals):
    if (g, s, b) == k_score:
        print(i + 1)
        break