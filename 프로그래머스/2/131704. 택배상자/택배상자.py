def solution(order):
    belt = []
    idx = 0
    answer = 0
    
    for box in range(1, len(order)+1):
        belt.append(box)
        
        while (belt) and (belt[-1] == order[idx]):
            belt.pop()
            answer += 1
            idx += 1
              
    return answer