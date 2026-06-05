# 해시[uid] = 이름

def solution(record):
    result = []
    users = dict()
    
    for sentence in record:
        if sentence[0] == 'L':
            word, uid = sentence.split()
            result.append((uid, "님이 나갔습니다."))
        else:
            word, uid, name = sentence.split()
            users[uid] = name
        
            if word == 'Enter':
                result.append((uid, "님이 들어왔습니다."))
                
        
    answer = []
    for u, s in result:
        answer.append(users[u] + s)
        
    return answer