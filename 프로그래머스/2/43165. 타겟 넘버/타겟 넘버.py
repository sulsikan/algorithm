# 전 풀이 참고
# 노드 엣지 구성의 그래프로 한번 생각해봐라
# 원하는 타겟이 나올 때 까지 탐색하는 dfs
answer = 0
def solution(numbers, target):
    dfs(0, 0, numbers, target)
    return answer

def dfs(idx, total, numbers, target):
    global answer
    if idx == len(numbers):
        if total == target:
            answer += 1
        return
    dfs(idx+1, total+numbers[idx], numbers, target)
    dfs(idx+1, total-numbers[idx], numbers, target)