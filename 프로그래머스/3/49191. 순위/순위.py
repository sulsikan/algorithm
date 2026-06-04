def solution(n, results):
    answer = 0

    players = [[0] * (n+1) for _ in range(n+1)]
    
    for winner, loser in results:
        players[winner][loser] = 1
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if players[i][k] == 1 and players[k][j] == 1:
                    players[i][j] = 1

    for i in range(1, n + 1):
        count = 0

        for j in range(1, n + 1):
            if players[i][j] or players[j][i]:
                count += 1

        if count == n - 1:
            answer += 1
        
    return answer