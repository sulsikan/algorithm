def solution(numbers, target):
    answer = 0
    
    def dfs(index, total):
        nonlocal answer
        
        if index + 1 == len(numbers):
            if total == target:
                answer += 1
            return
        
        dfs(index + 1, total + numbers[index + 1])
        dfs(index + 1, total - numbers[index + 1])

    dfs(0, numbers[0])
    dfs(0, - numbers[0])
        
    return answer