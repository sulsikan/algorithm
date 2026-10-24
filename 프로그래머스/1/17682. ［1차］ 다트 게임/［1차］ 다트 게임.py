def solution(dartResult):
    scores = []
    i = 0
    
    while i < len(dartResult):
        
        if dartResult[i:i+2] == '10':
            score = 10
            i += 2
        else:
            score = int(dartResult[i])
            i += 1
            
        bonus = dartResult[i]
        if bonus == 'D':
            score = score**2
        if bonus == 'T':
            score = score**3
        i += 1
            
        if i < len(dartResult) and dartResult[i] in "*#":
            
            if dartResult[i] == '*':
                score *= 2
                if scores:
                    scores[-1] *= 2
                    
            if dartResult[i] == '#':
                score *= -1
            
            i += 1
        
        scores.append(score)
    
    return sum(scores)