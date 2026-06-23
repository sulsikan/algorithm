def solution(triangle):
    answer = 0
    n = len(triangle)
    
    for i in range(1, n):
        for j in range(len(triangle[i])):
            # 맨 왼쪽 칸은 바로 위에서만 내려올 수 있음
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
            

    return max(triangle[-1])