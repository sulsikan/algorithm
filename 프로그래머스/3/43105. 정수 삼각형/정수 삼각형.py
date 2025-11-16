def solution(triangle):
    # triangle[i][j]에 최대합 갱신해서 저장
    n = len(triangle)
    for i in range(1, n):
        for j in  range(i+1):
            if j==i:
                triangle[i][i] += triangle[i-1][i-1]
            elif j==0:
                triangle[i][j] += triangle[i-1][0]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    
    return max(triangle[-1])