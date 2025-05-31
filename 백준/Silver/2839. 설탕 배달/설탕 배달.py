import sys
input = sys.stdin.readline

n = int(input())  # 설탕의 무게


# 5로 나누어 떨어질 때
if n % 5 == 0:
    print(n // 5)
else:
    cnt = 0  # 봉지의 개수
    while n > 0:
        n -= 3
        cnt += 1
        # 5와 3의 조합으로 될때
        if n % 5 == 0:
            cnt += n // 5
            print(cnt)
            break
        # 3만으로 될 때
        elif n == 0:
            print(cnt)
            break
        # 둘의 조합으로도 안될 때
        elif n ==1 or n == 2:
            print(-1)
            break