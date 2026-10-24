from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    # 모든 경우의 수 조합
    # len(dungeons)가 3개라면 3!
    numbers = [x for x in range(len(dungeons))]
    pm = permutations(numbers)

    for combi in pm:
        health = k
        stage_cnt = 0
        
        for stage in combi:
            # 먼저 최소 피로도 >= k를 충족하는지 본다.
            if health >= dungeons[stage][0]:
                # 충족한다면 소모 피로도 깎고 health 갱신한다
                health -= dungeons[stage][1]
                stage_cnt += 1
            else:
                break
                
        answer = max(answer, stage_cnt)
        
        
    return answer