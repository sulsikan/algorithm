import sys
input = sys.stdin.readline

n, k = map(int, input().split())
rank_list = {}
for _ in range(n):
    nation, gold, silver, bronze = map(int, input().split())
    rank_list[nation] = {"gold" : gold, "silver" : silver, "bronze":bronze}

sorted_rank = sorted(rank_list.items(), key=lambda x: (-x[1]["gold"], -x[1]["silver"], -x[1]["bronze"]))

prev_rank = 0
prev_score = None
ranking = []
for i, (n, m) in enumerate(sorted_rank):
    score = (m["gold"], m["silver"], m["bronze"])
    if score != prev_score:
        prev_rank += 1
        prev_score = score
    ranking.append((n, prev_rank, m))

for nation, rank, medal in ranking:
    if nation == k:
        print(rank)