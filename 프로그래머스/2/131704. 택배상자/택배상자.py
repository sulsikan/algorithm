# belt = [] <- 1, 2, 3, 4, 스택 마지막 번호 확인 후 옮기기(answer += 1)
def solution(order):
    belt = []
    idx = 0
    answer = 0
    
    for box in range(1, len(order) + 1):
        belt.append(box)
        
        while (belt) and (belt[-1] == order[idx]):
            answer += 1
            idx += 1
            belt.pop()

    return answer