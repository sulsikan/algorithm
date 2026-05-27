def solution(n, results):

    graph = [[False] * (n + 1) for _ in range(n + 1)]

    # 승패 기록
    for winner, loser in results:
        graph[winner][loser] = True

    # 플로이드 워셜
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):

                # a가 k를 이기고
                # k가 b를 이기면
                # a가 b를 이김
                if graph[a][k] and graph[k][b]:
                    graph[a][b] = True

    answer = 0

    for i in range(1, n + 1):
        count = 0

        for j in range(1, n + 1):
            if graph[i][j] or graph[j][i]:
                count += 1

        if count == n - 1:
            answer += 1

    return answer