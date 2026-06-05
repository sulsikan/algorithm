from collections import defaultdict, deque

import math

def solution(fees, records):
    answer = []
    calc_list = dict()
    accrue_car = defaultdict(int)
    queue = []
    
    for row in records:
        t, n, s = row.split()
        min_t = int(t[0:2]) * 60 + int(t[3:])

        if s == 'IN':
            calc_list[n] = min_t
            if n not in queue:
                queue.append(n)
                
        else:
            accrue_car[n] += min_t - calc_list[n]
            calc_list[n] = -1
        
    # 가격표 계산
    queue.sort()
    
    for car_num in queue:

        if calc_list[car_num] >= 0:
            accrue_car[car_num] += (23 * 60 + 59) - calc_list[car_num]
            
        if accrue_car[car_num] < fees[0]:
            answer.append(fees[1])
            continue
        
        answer.append(fees[1] + math.ceil((accrue_car[car_num] - fees[0]) / fees[2]) * fees[3])

    return answer