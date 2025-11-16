def solution(m, n, puddles):
    MOD = 1000000007
    
    # dp[y][x]: (1,1)에서 (x,y)까지 오는 경로 수
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # 물웅덩이 표시
    puddle = [[False] * (m + 1) for _ in range(n + 1)]
    for x, y in puddles:
        puddle[y][x] = True  # (열,행) → (x,y)
    
    dp[1][1] = 1  # 시작점
    
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if y == 1 and x == 1:
                continue  # 시작점은 이미 1로 설정
            if puddle[y][x]:
                dp[y][x] = 0
            else:
                dp[y][x] = (dp[y-1][x] + dp[y][x-1]) % MOD
    
    return dp[n][m]
