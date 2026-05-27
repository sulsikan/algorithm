# 플루이드워셜

def solution(n, results):
    win_result_table = [[False] * (n+1) for _ in range(n+1)]
    lose_result_table = [[False] * (n+1) for _ in range(n+1)]
    
    for win, lose in results:
        win_result_table[win][lose] = True
        lose_result_table[lose][win] = True
        
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                if win_result_table[i][k] and win_result_table[k][j]:
                    win_result_table[i][j] = True
                if lose_result_table[i][k] and lose_result_table[k][j]:
                    lose_result_table[i][j] = True
                    
    answer = 0
    
    for i in range(1, n+1):
        win_cnt = win_result_table[i].count(True)
        lose_cnt = lose_result_table[i].count(True)
        
        if win_cnt + lose_cnt == n-1:
            answer += 1

    return answer