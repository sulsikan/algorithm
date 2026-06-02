def solution(record):
    users = dict()
    result = []
    answer = []
    
    for sentence in record:
        sentence_split = sentence.split()
        
        # Enter, Change
        if len(sentence_split) == 3:
            users[sentence_split[1]] = sentence_split[2]
            
        result.append((sentence_split[0], sentence_split[1]))
            
    for word, uid in result:
        if word == 'Enter':
            answer.append(users[uid]+"님이 들어왔습니다.")
        elif word == 'Leave':
            answer.append(users[uid]+"님이 나갔습니다.")
    
    return answer