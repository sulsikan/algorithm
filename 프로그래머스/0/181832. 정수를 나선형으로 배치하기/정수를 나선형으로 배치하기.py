def solution(n: int):
    # n x n 0으로 초기화
    ans = [[0] * n for _ in range(n)]

    top, bottom = 0, n - 1
    left, right = 0, n - 1
    val = 1
    target = n * n

    while val <= target:
        # 1) 왼 -> 오
        for c in range(left, right + 1):
            ans[top][c] = val
            val += 1
        top += 1
        if val > target: break

        # 2) 위 -> 아래
        for r in range(top, bottom + 1):
            ans[r][right] = val
            val += 1
        right -= 1
        if val > target: break

        # 3) 오 -> 왼
        for c in range(right, left - 1, -1):
            ans[bottom][c] = val
            val += 1
        bottom -= 1
        if val > target: break

        # 4) 아래 -> 위
        for r in range(bottom, top - 1, -1):
            ans[r][left] = val
            val += 1
        left += 1

    return ans
