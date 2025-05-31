N = int(input())
dist = list(map(int, input().split()))
citys = list(map(int, input().split()))

cost = 0
min_price = citys[0]

for i in range(N - 1):
    # 최저가 갱신
    if citys[i] < min_price:
        min_price = citys[i]

    # 현재 최저가 적용해서 계산
    cost += min_price * dist[i]

print(cost)  # 총 비용 출력