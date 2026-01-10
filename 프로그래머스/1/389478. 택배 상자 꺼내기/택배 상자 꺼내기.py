def solution(n, w, num):
    # 박스를 먼저 쌓는다
    boxs = [[] for _ in range(w)]
    box_num = 0
    direction = 1
    
    while box_num < n:
        for idx in range(0, w, direction) if direction == 1 else range(w-1, -1, -1):
            box_num += 1
            boxs[idx].append(box_num)
            if box_num >= n:
                break
        direction *= -1
    
    for values in boxs:
        if num in values:
            answer = len(values) - values.index(num)
        
    return answer