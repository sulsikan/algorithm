import sys
input = sys.stdin.readline

n, l, d = map(int, input().split())
music_time = [0] * (n*l + (n-1)*5)
sec = 0
for _ in range(n):
    play_mc = True
    while play_mc and sec < len(music_time):
        # 멈추는 부분
        for i in range(1, n):
            if sec == (i*l + (i-1)*5) -1:
                play_mc = False
                break
        # 재생하는 부분
        music_time[sec] = 1
        sec += 1
    sec += 5


for i in range(d, len(music_time), d):
    if music_time[i] == 0:
        print(i)
        break
else:
    i = 1
    while True:
        if d * i >= len(music_time):
            print(d * i)
            break
        else:
            i += 1