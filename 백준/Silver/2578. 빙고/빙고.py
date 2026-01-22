import sys
input = sys.stdin.readline

board = [[] for _ in range(5)]
for i in range(5):
    board[i] = list(map(int, input().split()))

call = 0
stop = False

def bingo_count():
    cnt = 0

    # 가로
    for r in range(5):
        if board[r][0] == board[r][1] == board[r][2] == board[r][3] == board[r][4] == 0:
            cnt += 1

    # 세로
    for c in range(5):
        if board[0][c] == board[1][c] == board[2][c] == board[3][c] == board[4][c] == 0:
            cnt += 1

    # 메인 대각선
    if board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4] == 0:
        cnt += 1

    # 반대 대각선
    if board[0][4] == board[1][3] == board[2][2] == board[3][1] == board[4][0] == 0:
        cnt += 1

    return cnt


for _ in range(5):
    call_nums = list(map(int, input().split()))
    for cn in call_nums:
        call += 1

        # 숫자 지우기 (기존 방식 유지)
        for i in range(5):
            if cn in board[i]:
                board[i][board[i].index(cn)] = 0
                break

        # 현재 빙고 새로 계산
        if bingo_count() >= 3:
            stop = True
            break

    if stop:
        break

print(call)
