import sys
input = sys.stdin.readline

n = int(input())
currency = [25, 10, 5, 1]  # 화폐 단위

for i in range(n):
    result = []
    money = int(input())
    for c in currency:
        result.append(money // c)
        money %= c

    print(result[0], result[1], result[2], result[3])  # 쿼터, 다임, 니켈, 페니 순서로 출력