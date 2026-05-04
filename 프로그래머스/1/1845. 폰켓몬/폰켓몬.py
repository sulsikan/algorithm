from collections import defaultdict
def solution(nums):
    answer = 0
    ponketmons = defaultdict(int)
    
    for n in nums:
        ponketmons[n] += 1
    
    if len(ponketmons) > len(nums)//2:
        answer = len(nums)//2
    else:
        answer = len(ponketmons)
        
    return answer