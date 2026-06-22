from collections import defaultdict
import math

def solution(fees, records):
    calc_list = dict()
    accum_time = defaultdict(int)
    in_car = set()
    answer = []
    
    for row in records:
        time, car_num, state = row.split()
        min_time = int(time[0:2]) * 60 + int(time[3:])
        
        if state == 'IN':
            calc_list[car_num] = min_time
            in_car.add(car_num)
        else:
            accum_time[car_num] += min_time - calc_list[car_num]
            calc_list[car_num] = -1
            
    sorted_car_list = sorted(in_car)
            
    for car_num in sorted_car_list:
        if calc_list[car_num] >= 0:
            accum_time[car_num] += (23 * 60 + 59) - calc_list[car_num]
        
        if accum_time[car_num] < fees[0]:
            answer.append(fees[1])
            continue
            
        answer.append(fees[1] + math.ceil((accum_time[car_num] - fees[0]) / fees[2]) * fees[3])
        
    return answer
    
        
            
            
        