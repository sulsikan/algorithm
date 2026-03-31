#구현 #그리디
#판별 : 최적의 경우 탱크들이 길을 막아 돌아가는 경우는 없으므로 돌아가지 않고 탱크들을 정렬하는 방법을 찾는 것이 핵심이다.

import sys
input = sys.stdin.readline

n = int(input())
result = []
tanks = []
for i in range(n):
    r, c = map(int, input().split())
    tanks.append([i, r-1, c-1])

# 탱크들의 좌표를 입력받고 해당 탱크들을 x좌표 기준으로 오름 차순으로 정렬한다
tanks.sort(key=lambda x : x[1])

# 위로 가야하는 탱크와 아래로 가야하는 탱크의 배열을 만든다.
up_tank = []
down_tank = []
for i in range(n):
    if tanks[i][1] > i:
        up_tank.append(i)
    if tanks[i][1] < i:
        down_tank.append(i)
# 제일 아래에 있는 탱크부터 움직이도록 배열을 뒤집어준다.
down_tank.sort(reverse = True)

# 순서를 구분하지 않아도 되는 이유는 이미 위에서 충돌 날 만한 상황을 전부 순서대로 처리해 놨기 때문에 그대로 결과 배열에 넣기만 하면 된다.
for tank in up_tank:
    for _ in range(tank, tanks[tank][1]):
        result.append((tanks[tank][0]+1, "U"))
        tanks[tank][1] = tank

for tank in down_tank:
    for _ in range(tanks[tank][1], tank):
        result.append((tanks[tank][0]+1, "D"))
        tanks[tank][1] = tank

# 좌우도 똑같이 하면 됨
tanks.sort(key=lambda x : x[2])

left_tank = []
right_tank = []
for i in range(n):
    if tanks[i][2] > i:
        left_tank.append(i)
    if tanks[i][2] < i:
        right_tank.append(i)

right_tank.sort(reverse = True)

for tank in left_tank:
    for _ in range(tank, tanks[tank][2]):
        result.append((tanks[tank][0]+1, "L"))
        tanks[tank][2] = tank

for tank in right_tank:
    for _ in range(tanks[tank][2], tank):
        result.append((tanks[tank][0]+1, "R"))
        tanks[tank][2] = tank

print(len(result))
for tank, move in result:
    print(tank, move)