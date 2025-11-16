def solution(N, number):
    dp = [set() for _ in range(9)]
    
    if N == number:
        return 1
    
    for k in range(1,9):
        # 1) NNN...N (붙이기) 추가
        dp[k].add(int(str(N)*k))
        
        # 2) 두 집합 조합 (i + (k-i))
        for i in range(1, k):
            for a in dp[i]:
                for b in dp[k-i]:
                    dp[k].add(a + b)
                    dp[k].add(a - b)
                    dp[k].add(a * b)
                    if b != 0:
                        dp[k].add(a//b)
                        
        if number in dp[k]:
            return k
        
    return -1


