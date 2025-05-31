import sys 
input = sys.stdin.readline

n = int(input())  # 물품가격
cnt = 0
currency = [500, 100, 50, 10, 5, 1]  # 화폐 단위

k = 1000 - n  # 거스름돈
for c in currency:
    cnt += (k // c)
    k %= c

print(cnt)  # 잔돈의 개수 출력