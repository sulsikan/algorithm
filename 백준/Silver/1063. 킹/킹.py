import sys

def move(cmd, x, y):
    # R : 한 칸 오른쪽으로
    if 'R' in cmd:
            x += 1

    # L : 한 칸 왼쪽으로
    elif 'L' in cmd:
            x -= 1

    # B : 한 칸 아래로
    if 'B' in cmd:
            y -= 1

    # T : 한 칸 위로
    elif 'T' in cmd:
            y += 1

    return x, y

input = sys.stdin.readline
king, stone, n = input().split()
king = list(king)
stone = list(stone)
n = int(n)

direction = [input().strip() for _ in range(n)]

col_name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# 죄표정보를 숫자로 변환
for i in range(8):
    if col_name[i] == king[0]:
        king[0] = int(i)
        king[1] = int(king[1])-1
    if col_name[i] == stone[0]:
        stone[0] = int(i)
        stone[1] = int(stone[1])-1

for cmd in direction:
    cmd = list(cmd)
    tmp_k_x, tmp_k_y, tmp_s_x, tmp_s_y = king[0], king[1], stone[0], stone[1]
    tmp_k_x, tmp_k_y = move(cmd, tmp_k_x, tmp_k_y)
    # 도착 지점에 돌이 있을 때 돌 밀어내기
    if tmp_k_x == tmp_s_x and tmp_k_y == tmp_s_y:
        tmp_s_x, tmp_s_y = move(cmd, tmp_s_x, tmp_s_y)
    # 체스판 8*8 범위 벗어나면 이동 취소
    if 0 <= tmp_k_x <= 7 and 0 <= tmp_k_y <= 7 and 0 <= tmp_s_x <= 7 and 0 <= tmp_s_y <= 7:
        king[0] = tmp_k_x
        king[1] = tmp_k_y
        stone[0] = tmp_s_x
        stone[1] = tmp_s_y

print(col_name[king[0]]+str(king[1]+1))
print(col_name[stone[0]]+str(stone[1]+1))


