# input
n, k = map(int, input().split())
medals = [list(map(int, input().split())) for _ in  range(n)]

# rank 매기기
medals.sort(key=lambda x : (x[1], x[2], x[3]), reverse = True)

# 동점 국가 검사
chk_medal = medals
tie_cnt = 0
prev_score = []
for nation, g, s, b in medals:
    score = (g, s, b)
    if nation == k:
        if score in prev_score:
            tie_cnt += 1
    prev_score.append(score)

# k 국가 찾기
idx = [medals[i][0] for i in range(n)].index(k)


# 결과 반환
print(idx - tie_cnt + 1)