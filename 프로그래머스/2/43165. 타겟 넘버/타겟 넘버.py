# 노드 엣지 구성의 그래프로 생각하면 원하는 타겟이 나올때까지 탐색하는 dfs 문제로 풀이 가능
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    def dfs(idx, total):
        nonlocal answer
        if idx == n:
            if total == target:
                answer += 1
            return
        dfs(idx+1, total+numbers[idx])
        dfs(idx+1, total-numbers[idx])
        
    dfs(0,0)

    return answer
