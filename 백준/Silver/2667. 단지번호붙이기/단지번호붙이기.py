'''
1. 아이디어
- 이중 for문 > 원소 1 && 방문한적 없음 > DFS실행, 단지 수++ > DFS결과 집 수 목록에 저장

2. 시간복잡도
DFS = O(V+E)
V + E = N^2 + 4N^2 = 5N^2
--> O(5N^2) = O(N^2) <= 625
2억 미만이니 가능

3. 자료구조
단지 수 int
지도 int[][]
방문확인 bool[][]
단지별 집 수 int[]
'''

import sys
input = sys.stdin.readline

N = int(input())
map = [list(map(int, input().strip())) for _ in range(N)]
chk = [[False] * N for _ in range(N)]
result = []
# 전역변수
each = 0

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y, x):
    global each     # each는 전역변수기 때문에 함수 안에서 사용하려면 전역벽수로 바꿔주는 과정 필요함
    each += 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if map[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                dfs(ny, nx)

for j in range(N):
    for i in range(N):
        if map[j][i] == 1 and chk[j][i] == False:
            # 방문 체크 표시
            chk[j][i] = True
            # DFS로 크기 구하기(함수에서 리턴값을 받아오는 것보다 전역변수를 사용하는 것이 편함)
            each = 0
            dfs(j, i)
            result.append(each)

result.sort()
print(len(result))
for i in result:
    print(i)