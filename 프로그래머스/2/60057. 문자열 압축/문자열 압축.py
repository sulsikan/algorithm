def solution(s):
    answer = len(s)
    
    for num in range(1, len(s)//2 + 1):
        result = ''
        count = 1
        
        now = s[:num]
        
        for i in range(num, len(s), num):
            nxt = s[i:i + num]
            
            if nxt == now:
                count += 1
            else:
                if count == 1:
                    result += now
                else:
                    result += str(count) + now
                now = nxt
                count = 1
                
        if count > 1:
            result += str(count) + now
        else:
            result += now
        answer = min(answer, len(result))
        result = ''
        
    return answer