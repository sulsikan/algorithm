def solution(s):
    answer = len(s)
    
    for num in range(1, len(s)//2+1):
        result = ''
        cnt = 1
        now = s[:num]
        
        for i in range(num, len(s), num):
            nxt = s[i:i + num]
            
            if now == nxt:
                cnt += 1
            else:
                if cnt == 1:
                    result += now
                else:
                    result += str(cnt) + now
                now = nxt
                cnt = 1
                
        if cnt > 1:
            result += str(cnt) + now
        else:
            result += now
            
        answer = min(answer, len(result))
        result = ''
        
    return answer