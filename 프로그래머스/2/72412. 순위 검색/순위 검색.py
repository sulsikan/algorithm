from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    db = defaultdict(list)

    # 1. info 전처리
    for i in info:
        data = i.split()
        conditions = data[:-1]          # 언어, 직군, 경력, 음식
        score = int(data[-1])           # 점수

        # 조건 4개 중 일부를 '-'로 바꾸는 모든 경우 생성
        for r in range(5):
            for comb in combinations(range(4), r):
                temp = conditions[:]

                for idx in comb:
                    temp[idx] = '-'

                key = ''.join(temp)
                db[key].append(score)

    # 2. 각 key별 점수 리스트 정렬
    for key in db:
        db[key].sort()

    answer = []

    # 3. query 처리
    for q in query:
        q = q.replace(' and ', ' ')
        data = q.split()

        key = ''.join(data[:-1])
        score = int(data[-1])

        scores = db[key]

        # score 이상인 첫 위치
        idx = bisect_left(scores, score)

        # 전체 개수 - 첫 위치 = score 이상인 사람 수
        answer.append(len(scores) - idx)

    return answer